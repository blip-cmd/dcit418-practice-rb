import json
import unittest
from pathlib import Path
from scripts.parse_management_bank import (
    PART_TITLES,
    parse_sakai_and_mba,
    parse_it_class,
)


class ManagementParserTests(unittest.TestCase):
    def test_sakai_parser(self):
        sakai_path = Path("bd/dcit402-sakai-quiz1.md")
        if sakai_path.exists():
            qs = parse_sakai_and_mba(sakai_path, "sakai")
            self.assertEqual(len(qs), 60)
            for q in qs:
                self.assertTrue(q["id"].startswith("sakai-"))
                self.assertEqual(q["batch"], "sakai")
                self.assertGreater(len(q["options"]), 0)

    def test_part_titles(self):
        self.assertEqual(len(PART_TITLES), 6)
        self.assertEqual(PART_TITLES[1], "Management Foundations")
        self.assertEqual(PART_TITLES[6], "Evolution of Management")

    def test_questions_json_integrity(self):
        json_path = Path("questions.json")
        self.assertTrue(json_path.exists())
        data = json.loads(json_path.read_text(encoding="utf-8"))
        self.assertEqual(len(data), 621)
        parts = {q["part"] for q in data}
        self.assertEqual(parts, {1, 2, 3, 4, 5, 6})
        for q in data:
            self.assertTrue(q["id"].startswith("P"))
            self.assertTrue(1 <= q["part"] <= 6)
            self.assertTrue(len(q["bodyMarkdown"]) > 0)
            self.assertIn(q["type"], ["mcq4", "mcq5", "fill", "tf"])


if __name__ == "__main__":
    unittest.main()
