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

    def test_all_programmes_mapped_without_losing_source_outcomes(self):
        data = eef.load_json(ROOT / 'datasets/eef/programmes.json')['programmes']
        self.assertEqual(len(data), 24)
        self.assertTrue(all(p['entries'] for p in data.values()))
        raw = eef.load_json(ROOT / 'raw/EEF/EEF_promising_programmes_full .json')
        supplement = eef.load_json(ROOT / 'raw/EEF/EEF_promising_programmes_补充.json')
        source = {(t['url'], o['outcome_group']): o for t in raw['trials'] + supplement['trials'] for o in t.get('trial_outcomes', [])}
        actual = {(t['url'], o['outcome_group']): o for p in data.values() for t in p['trials'] for o in t.get('outcomes', [])}
        self.assertEqual(set(source), set(actual))
        for key, original in source.items():
            for field in ('impact_months', 'effect_size', 'security_strength', 'security_status'):
                self.assertEqual(actual[key].get(field), original.get(field), (key, field))
        p = data['tutor-trust-primary']
        self.assertIn('£112/生/干预周期', eef.render_programme('tutor-trust-primary', p, [], {}))
        self.assertIn('小幅正向影响', eef.render_programme('emotion-coaching', data['emotion-coaching'], [], {}))

    def test_visible_classroom_is_evaluation_with_negative_and_zero_results(self):
        data = eef.load_json(ROOT / 'datasets/eef/programmes.json')['programmes']
        p = data['the-visible-classroom-2015']
        self.assertIs(p['is_promising'], False)
        result = eef.render_programme('the-visible-classroom-2015', p, [], {})
        self.assertIn('[!eef-programme|evaluation]', result)
        self.assertNotIn('[!eef-programme|v3]', result)
        pilot, trial = result.split('[!eef-trial]-')[1:]
        self.assertIn('实施 2014-03 至 2014-07', pilot)
        self.assertIn('36 名教师', pilot)
        self.assertIn('干预 2014-03 至 2014-07', pilot)
        self.assertIn('报告日期 2015-02', pilot)
        self.assertNotIn(eef.PENDING, pilot)
        self.assertNotIn('2013-02 至 2016-01', pilot)
        self.assertNotIn('EEF_Project_Protocol_Visible_Classroom.pdf', pilot)
        self.assertNotIn('EEF_Project_Protocol_Regrant_Visible_Classroom.pdf', trial)
        self.assertNotIn('Regrant_-_Visible_Classroom_AMENDED_1.pdf', trial)
        self.assertNotIn('Visible_Classroom_SAP.pdf', trial)
        self.assertIn('Visible_Classroom.pdf', trial)
        self.assertNotIn('EEF_Project_Protocol_Visible_Classroom.pdf', trial)
        self.assertNotIn('2016 年方案目标为 140 所学校、11,760 名学生', trial)
        self.assertIn('7,230 名学生', trial)
        self.assertIn('£367/生/年', pilot)
        self.assertNotIn('| out |', pilot)
        self.assertIn('试验 2016-04 至 2018-07；干预 2016-09 至 2018-06', trial)
        self.assertIn('| -1 | -0.09', trial)
        self.assertIn('| -1 | -0.05', trial)
        self.assertIn('| 0 | -0.03', trial)
        self.assertIn('| 0 | 0.03', trial)
        self.assertIn('[-0.25, -0.01]', trial)
        self.assertIn('p = 0.04；负向显著', trial)
        self.assertIn('[-0.23, 0.17]', trial)
        self.assertIn('| out | grp | imp | es | ci | sec | sig |', trial)
        self.assertIn('| -0.13 | [-0.25, -0.01] |', trial)
        self.assertNotIn('95%置信区间 [', trial)
        self.assertIn('n = 1,232', trial)
        self.assertIn('最终分析 6,934 人', trial)
        self.assertNotIn('页面学校数', result)
        self.assertIn('招募 10 所小学', pilot)
        self.assertIn('随机分配 86 所学校（干预组 44 所，对照组 42 所）', trial)
        self.assertIn('原五年级 83 校、3,337 人，原六年级 85 校、3,597 人', trial)
        outcome_table = trial.split('| out | grp |')[1]
        self.assertLess(outcome_table.index('原五年级队列'), outcome_table.index('↳ 原五年级免费校餐资格学生'))
        self.assertLess(outcome_table.index('↳ 原五年级免费校餐资格学生'), outcome_table.index('原六年级队列'))
        self.assertIn('依从分析和缺失基线复核未改变综合成绩结论', trial)
        self.assertIn('对照组无对应评分', trial)
        self.assertNotIn('研究拨款 TBC', result)
        self.assertIn('研究拨款 ' + eef.PENDING, result)
        self.assertEqual(result.count(eef.PENDING), 1)
        self.assertIn('EEF 网页尚未公布金额', result)
        self.assertEqual(result.count('[!eef-errata]'), 1)
        self.assertIn('[!eef-errata]- 资料缺漏与差异', result)
        funding = trial.split('| 经费 |', 1)[1].splitlines()[0]
        self.assertNotIn('待核实', funding)
        self.assertNotIn('口径不一致', funding)
        self.assertNotIn('5 项待核实', result)
        self.assertIn('报告日期 2021-02', trial)
        self.assertEqual(pilot.count('> > > [!'), 1)
        self.assertEqual(trial.count('> > > [!'), 1)
        self.assertIn('关键发现与局限', pilot)
        self.assertIn('关键局限', trial)
        for title in ('补充分析', '原方案的交付安排', '方案修订与分析预设', '原方案的功效假设',
                      '分析计划中的样本记录', '分析计划中的随机分层记录', '研究时程', '三批实施安排'):
            self.assertNotIn(f'[!ref-table]- {title}', result)

    def test_confidence_interval_column_preserves_zero_and_missing_bounds(self):
        p = copy.deepcopy(self.programme)
        p['trials'] = p['trials'][:1]
        rows = copy.deepcopy(p['trials'][0]['outcomes'])
        rows[0].update(effect_size=0, ci_lower=0, ci_upper=0)
        rows[1].update(effect_size=.1, ci_lower=-.1, ci_upper=None)
        p['trials'][0]['record']['outcomes'] = rows
        result = eef.render_programme(SLUG, p, [], {})
        self.assertIn('| es | ci | sec |', result)
        self.assertIn('| 0 | [0, 0] |', result)
        self.assertIn('| 0.1 | 未提供 |', result)
        self.assertNotIn('[-0.1, 0]', result)
        rows[0].pop('ci_upper')
        result = eef.render_programme(SLUG, p, [], {})
        self.assertNotIn('| ci |', result)

    def test_visible_classroom_follows_programme_template_order(self):
        note = (ROOT / 'wiki/facts/uk/Visible Classroom Programme.md').read_text()
        background = note.split('> [!program-context] 项目背景\n', 1)[1].split('\n---\n', 1)[0]
        self.assertEqual(len([line for line in background.splitlines() if line.startswith('> - **')]), 4)
        design = note.split('> [!policy-design] 方案设计\n', 1)[1].split('\n---\n', 1)[0]
        self.assertEqual([line.split('**')[1] for line in design.splitlines() if line.startswith('> - **')],
                         ['项目目标', '覆盖对象', '干预措施', '实施控制'])
        self.assertLess(note.index('> [!claim] 核心干预假说'), note.index('> [!policy-design]'))
        self.assertLess(note.index('> [!pathways]'), note.index('> [!eef-programme'))
        self.assertLess(note.index('> [!policy-design]'), note.index('> [!timeline]'))
        self.assertLess(note.index('> [!timeline]'), note.index('> [!actor-grid]'))
        self.assertNotIn('\n> [!ref-table]', note)
        self.assertNotIn('\n> [!figure]', note)
        module = eef.PROGRAMME_BLOCK_RE.search(note)
        self.assertIsNotNone(module)
        self.assertTrue(note[module.end():].lstrip().startswith('> [!finding-cards]'))
        self.assertNotIn('\n## ', note)

    def test_report_rows_do_not_overwrite_web_export_or_derive_months(self):
        p = eef.load_json(ROOT / 'datasets/eef/programmes.json')['programmes']['the-visible-classroom-2015']
        trial = p['trials'][1]
        self.assertEqual(len(trial['outcomes']), 4)
        self.assertTrue(all(o['effect_size'] is None for o in trial['outcomes']))
        verified = trial['record']['outcomes']
        self.assertEqual(len(verified), 8)
        self.assertEqual(sum(o['sample_n'] for o in verified if o['security_status'] == 'ok'), 6934)
        reading = next(o for o in verified if o['group_zh'] == '原五年级队列' and o['label_zh'] == '阅读成绩')
        self.assertEqual(reading['impact_months'], -2)
        self.assertEqual(reading['effect_measure'], 'Hedges g')
        self.assertIsNone(next(o for o in verified if o['label_zh'] == '数学成绩')['impact_months'])
        unchanged = copy.deepcopy(p)
        eef.render_programme('the-visible-classroom-2015', p, [], {})
        self.assertEqual(p, unchanged)

    def test_project_period_supports_years_or_months_without_observed_dates(self):
        self.assertIn('2012-01 至 2014-01', eef.programme_project_period({'page_project_duration': '2 year(s)', 'completed': '2014-01'}))
        self.assertIn('2023-02 至 2023-12', eef.programme_project_period({'page_project_duration': '10 month(s)', 'completed': '2023-12'}))
        self.assertIsNone(eef.programme_project_period({'page_project_duration': '', 'completed': '2014-01'}))

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
