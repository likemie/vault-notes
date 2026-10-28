"""Corporate creators retain their formal names in APA metadata."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import vault_lint


class CorporateAuthorTests(unittest.TestCase):
    def test_team_is_a_corporate_creator(self):
        self.assertTrue(vault_lint.looks_like_organization_creator("Behavioural Insights Team"))

    def test_person_still_requires_inverted_name(self):
        for name in ("Amy Skipp", "Emily Tanner", "Tim Teammann"):
            with self.subTest(name=name):
                self.assertFalse(vault_lint.looks_like_organization_creator(name))


if __name__ == "__main__":
    unittest.main()
