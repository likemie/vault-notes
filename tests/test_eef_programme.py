"""Single-programme import and generated module regression checks."""
import contextlib
import copy
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import eef_sync as eef

SLUG = '1stclass-number-1'


class ProgrammeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.programme = json.loads((ROOT / 'datasets/eef/programmes.json').read_text())['programmes'][SLUG]
        raw = json.loads((ROOT / 'raw/EEF/EEF_promising_programmes_full .json').read_text())
        programme = next(p for p in raw['programmes'] if p['url'].endswith('/' + SLUG))
        cls.raw = {**raw, 'programmes': [programme],
                   'trials': [t for t in raw['trials'] if t['url'] in programme['trial_urls']]}

    def test_render_separates_trial_and_outcome_counts(self):
        result = eef.render_programme(SLUG, self.programme, [], {})
        self.assertIn('[!eef-programme|v3]', result)
        self.assertEqual(result.count('[!eef-trial]-'), 2)
        self.assertEqual(result.count('| ↳ 免费校餐资格学生 |'), 2)
        body = result.split('[!eef-errata]')[0]
        first, second = body.split('[!eef-trial]-')[1:]
        self.assertIn('数量推理', first)
        self.assertNotIn('数学成绩', first)
        self.assertIn('数学成绩', second)
        self.assertNotIn('数量推理', second)
        self.assertNotIn('数据版本', result)
        self.assertIn('牛津大学', first)
        self.assertIn('NFER', second)
        self.assertIn('£77/生/年', first)
        self.assertIn('£93/生/年', second)
        self.assertIn('| 样本 | 页面学校数 235 所；随机分配学校 226 所', result)
        self.assertEqual(result.count('1,880'), 1)
        self.assertNotIn('2,412', result)
        self.assertNotIn('365', result)
        self.assertIn('未达统计显著', result)

    def test_inferred_project_period_never_fills_observed_dates(self):
        p = copy.deepcopy(self.programme)
        original = copy.deepcopy(p)
        result = eef.render_programme(SLUG, p, [], {})
        self.assertIn('2015-11 至 2018-07', result)
        self.assertIn('起点按周期倒推', result)
        self.assertIn('| 时间 | 试验 ' + eef.PENDING, result)
        self.assertIn('干预 ' + eef.PENDING, result)
        self.assertEqual(p, original)
        self.assertIsNone(eef.programme_project_period({'page_project_duration': '2 year(s) 8 month(s)'}))
        self.assertIsNone(eef.programme_project_period({'page_project_duration': '2 year(s) 8 month(s)', 'completed': '2018-99'}))
        self.assertEqual(eef.programme_date_range({'study_start': '2016-01'}, 'study'), '2016-01 至 ' + eef.PENDING)

    def test_supplementary_sources_do_not_repeat_trial_fields(self):
        result = eef.render_programme(SLUG, self.programme, [], {})
        self.assertIn('英国国家教育研究基金会（National Foundation for Educational Research，NFER）', result)
        self.assertNotIn('起止日期未提供', result)
        self.assertNotIn('2 year(s)', result)
        self.assertEqual(result.count('学校首年 £1,612'), 1)
        self.assertEqual(result.count('假定每年实施两组'), 1)
        self.assertEqual(result.count('[!eef-errata]'), 1)
        body = result.split('[!eef-errata]')[0]
        first, second = body.split('[!eef-trial]-')[1:]
        for trial, record in zip((first, second), self.programme['trials']):
            for key in ('时间', '评估', '样本', '剂量', '培训', '经费', '资料'):
                self.assertEqual(trial.count(f'| {key} |'), 1, key)
            self.assertLess(trial.index('| 样本 |'), trial.index('| out |'))
            self.assertLess(trial.index('| 资料 |'), trial.index('| out |'))
            for context in record['record']['sample_context']:
                self.assertIn(context, trial)
            for document in record['documents']:
                self.assertIn(document['url'], trial)

    def test_zero_missing_and_unrated_remain_distinct(self):
        p = copy.deepcopy(self.programme)
        outcome = p['trials'][0]['outcomes'][0]
        outcome.update(impact_months=0, effect_size=0, security_strength=None,
                       security_status='not_rated', significance='未报告')
        result = eef.render_programme(SLUG, p, [], {})
        self.assertIn('| 0 | 0 | 未评级 |', result)
        self.assertIn('不适用', result)
        self.assertIn('未提供', result)
        self.assertEqual(eef.programme_rating(4, 5, 'not_applicable'), '不适用')
        self.assertEqual(eef.programme_months(None), '未提供')

    def test_qualitative_impact_is_not_zero_months(self):
        p = copy.deepcopy(self.programme)
        p.update(months=None, impact_label='小幅正向影响')
        result = eef.render_programme(SLUG, p, [], {})
        self.assertIn('| 小幅正向影响 |', result)
        self.assertNotIn('| 0 个月 |', result)

    def test_targeted_import_preserves_others_and_invalidates_changed_result(self):
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory)
            database, source = folder / 'programmes.json', folder / 'raw.json'
            sentinel = {'entries': ['keep.md'], 'name': 'keep exactly', 'trials': []}
            eef.dump_json(database, {'programmes': {'other-programme': sentinel, SLUG: self.programme}})
            raw = copy.deepcopy(self.raw)
            source.write_text(json.dumps(raw), encoding='utf-8')
            args = SimpleNamespace(raw=str(source), slug=SLUG)
            with patch.object(eef, 'PROG_JSON', database), contextlib.redirect_stdout(io.StringIO()):
                eef.cmd_import_programmes(args)
                imported = eef.load_json(database)['programmes']
                self.assertEqual(imported['other-programme'], sentinel)
                self.assertEqual(imported[SLUG]['entries'], self.programme['entries'])
                self.assertEqual(imported[SLUG]['trials'][0]['outcomes'][0]['significance'], '未达统计显著')
                trial = next(t for t in raw['trials'] if t['url'].endswith('/1stclassnumber'))
                trial['trial_outcomes'][0]['effect_size'] = .99
                source.write_text(json.dumps(raw), encoding='utf-8')
                eef.cmd_import_programmes(args)
                changed = eef.load_json(database)['programmes'][SLUG]
                self.assertNotIn('significance', changed['trials'][0]['outcomes'][0])
                self.assertNotIn('record', changed['trials'][0])

    def test_check_is_read_only_and_render_is_idempotent(self):
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory)
            note = folder / 'programme.md'
            original = '# Keep title\n\n## 成效评估\n\n### Keep analysis\n\nKeep prose.\n'
            note.write_text(original)
            p = copy.deepcopy(self.programme)
            p['entries'] = ['programme.md']
            database = folder / 'programmes.json'
            eef.dump_json(database, {'programmes': {SLUG: p}})
            with (patch.object(eef, 'ROOT', folder), patch.object(eef, 'PROG_JSON', database),
                  patch.object(eef, 'ERRATA_JSON', folder / 'absent.json'),
                  contextlib.redirect_stdout(io.StringIO())):
                self.assertEqual(eef.cmd_render_programmes(SimpleNamespace(check=True)), 1)
                self.assertEqual(note.read_text(), original)
                self.assertEqual(eef.cmd_render_programmes(SimpleNamespace(check=False)), 0)
                rendered = note.read_text()
                self.assertTrue(rendered.startswith('# Keep title\n\n## 成效评估\n'))
                self.assertTrue(rendered.endswith('### Keep analysis\n\nKeep prose.\n'))
                self.assertEqual(eef.cmd_render_programmes(SimpleNamespace(check=True)), 0)
                eef.cmd_render_programmes(SimpleNamespace(check=False))
                self.assertEqual(note.read_text(), rendered)
                self.assertEqual(rendered.count('[!eef-programme|v3]'), 1)


    def test_card_inserts_before_finding_cards_without_h2(self):
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory)
            note = folder / 'programme.md'
            original = '---\n\n> [!claim] 项目定位\n> x\n\n---\n\n> [!finding-cards] 核心实证结论\n> - y\n\n---\n\n> [!entry-map] 相关条目网络\n'
            note.write_text(original)
            p = copy.deepcopy(self.programme); p['entries'] = ['programme.md']
            database = folder / 'programmes.json'
            eef.dump_json(database, {'programmes': {SLUG: p}})
            with (patch.object(eef, 'ROOT', folder), patch.object(eef, 'PROG_JSON', database),
                  patch.object(eef, 'ERRATA_JSON', folder / 'absent.json'),
                  contextlib.redirect_stdout(io.StringIO())):
                eef.cmd_render_programmes(SimpleNamespace(check=False))
            rendered = note.read_text()
            self.assertLess(rendered.index('[!eef-programme|v3]'), rendered.index('[!finding-cards]'))
            self.assertNotIn('## ', rendered)

    def test_cost_rating_programme_and_trials(self):
        result = eef.render_programme(SLUG, self.programme, [], {})
        self.assertIn('| <span class="eef-cost">●●○○○ 低</span><br><small>£93/生/年</small> |', result)
        first, second = result.split('[!eef-errata]')[0].split('[!eef-trial]-')[1:]
        self.assertIn('成本评级 <span class="eef-cost">●○○○○ 极低</span>', first)
        self.assertIn('成本评级 <span class="eef-cost">●●○○○ 低</span>', second)
        self.assertEqual(eef._cost_rating(None, 5, 'not_rated'), '未评级')
        self.assertEqual(eef._cost_rating(None, 5, 'not_provided'), '未提供')


if __name__ == '__main__':
    unittest.main()
