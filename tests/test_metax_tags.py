import importlib.util
from pathlib import Path
import unittest
import yaml

spec = importlib.util.spec_from_file_location("metax_sync", Path(__file__).parents[1] / "scripts/metax_sync.py")
metax = importlib.util.module_from_spec(spec)
spec.loader.exec_module(metax)


class MetaXTagTests(unittest.TestCase):
    def check_tags(self, field, expected, present=True):
        text = "---\ntitle: Example\naliases:\n  - metax\n" + field + "\nstatus: draft\n---\n\nUnchanged body.\n"
        result = metax.set_tag(text, present)
        parsed = yaml.safe_load(result.split("---\n", 2)[1])
        self.assertEqual(parsed["tags"], expected)
        self.assertEqual(parsed["aliases"], ["metax"])
        self.assertEqual(parsed["status"], "draft")
        self.assertEqual(result.split("---\n", 2)[2], "\nUnchanged body.\n")
        self.assertEqual(metax.set_tag(result, present), result)

    def test_indentless_list_and_mixed_indent_failure(self):
        self.check_tags("tags:\n- theme/cross-cultural\n- level/k12", ["theme/cross-cultural", "level/k12", "metax"])
        self.check_tags("tags:\n  - metax\n- theme/cross-cultural\n- level/k12", ["theme/cross-cultural", "level/k12", "metax"])

    def test_indented_comments_duplicates_and_removal(self):
        self.check_tags("tags:\n  # keep this comment\n  - theme/topic\n  - metax\n  - metax", ["theme/topic", "metax"])
        self.check_tags("tags:\n- metax\n- theme/topic", ["theme/topic"], False)
        self.check_tags("tags:\n  - metax", [], False)

    def test_flow_scalar_and_empty_tags(self):
        self.check_tags('tags: ["topic, label", \'metax\']', ["topic, label", "metax"])
        self.check_tags('tags: [topic, "metax"]', ["topic"], False)
        self.check_tags("tags: []", ["metax"])
        self.check_tags("tags: topic", ["topic", "metax"])
        self.check_tags("tags: metax", [], False)

    def test_missing_tags_does_not_match_aliases(self):
        result = metax.set_tag("---\naliases:\n  - metax\n---\nbody\n", True)
        self.assertEqual(yaml.safe_load(result.split("---\n", 2)[1])["tags"], ["metax"])


if __name__ == "__main__":
    unittest.main()
