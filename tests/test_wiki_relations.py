from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import wiki_relations as relations


class IncrementalExtractedToTests(unittest.TestCase):
    def test_only_affected_sources_are_updated_once(self) -> None:
        source_paths = {
            "Source A": Path("/tmp/source-a.md"),
            "Source B": Path("/tmp/source-b.md"),
            "Source C": Path("/tmp/source-c.md"),
        }
        links = {
            title: relations.canonical_source_link(path, title)
            for title, path in source_paths.items()
        }
        original = {
            source_paths["Source A"]: ["[[Argument One]]", "[[Other Argument]]"],
            source_paths["Source B"]: [],
            source_paths["Source C"]: ["[[Argument One]]"],
        }
        writes: dict[Path, list[str]] = {}

        def record_update(path: Path, values: list[str], **_: object) -> bool:
            writes[path] = list(values)
            return True

        changed_entries = [
            (
                relations.Entry("Argument One", "wiki/arguments/Argument One.md", "argument"),
                Path("wiki/arguments/Argument One.md"),
                [links["Source B"]],
            )
        ]

        with (
            patch.object(relations, "current_extracted_to", side_effect=lambda path: list(original[path])),
            patch.object(relations, "update_source_extracted_to", side_effect=record_update),
        ):
            changed = relations.sync_extracted_to_incremental(
                changed_entries,
                source_paths,
                dry_run=False,
                add_missing=True,
            )

        self.assertEqual(3, changed)
        self.assertEqual(
            {
                source_paths["Source A"]: ["[[Other Argument]]"],
                source_paths["Source B"]: ["[[Argument One]]"],
                source_paths["Source C"]: [],
            },
            writes,
        )


if __name__ == "__main__":
    unittest.main()
