import json
import unittest
from pathlib import Path
from scripts.parse_security_bank import (
    PART_TITLES,
    classify_part,
    parse_bank,
)


class SecurityParserTests(unittest.TestCase):
    def test_quiz_bank_parser(self):
        quiz_path = Path("data_files/quiz_bank/quiz.md")
        if quiz_path.exists():
            qs = parse_bank(quiz_path, "quizbank")
            self.assertGreater(len(qs), 300)
            for q in qs:
                self.assertTrue(q["id"].startswith("quizbank-"))
                self.assertEqual(q["batch"], "quizbank")
                self.assertIn(q["type"], ["mcq4", "mcq5", "multi", "fill", "tf"])

    def test_ia_bank_parser(self):
        ia_path = Path("data_files/ia_bank/ia_clean.md")
        if ia_path.exists():
            qs = parse_bank(ia_path, "iabank")
            self.assertGreater(len(qs), 100)
            for q in qs:
                self.assertTrue(q["id"].startswith("iabank-"))
                self.assertEqual(q["batch"], "iabank")

    def test_part_titles(self):
        self.assertEqual(len(PART_TITLES), 14)
        self.assertEqual(PART_TITLES[0], "Data Protection & IT Security Policy")
        self.assertEqual(PART_TITLES[13], "Digital Signatures")

    def test_classify_part(self):
        self.assertEqual(classify_part("The AES round transformation SubBytes", ""), 5)
        self.assertEqual(
            classify_part("Which element of the IT security policy framework requires upper management approval?", ""),
            0,
        )
        self.assertEqual(classify_part("RSA encryption of message M is", ""), 9)

    def test_questions_json_integrity(self):
        json_path = Path("questions.json")
        self.assertTrue(json_path.exists())
        data = json.loads(json_path.read_text(encoding="utf-8"))
        self.assertGreater(len(data), 500)
        parts = {q["part"] for q in data}
        self.assertTrue(parts.issubset(set(range(14))))
        for q in data:
            self.assertTrue(q["id"].startswith("P"))
            self.assertTrue(0 <= q["part"] <= 13)
            self.assertTrue(len(q["bodyMarkdown"]) > 0)
            self.assertIn(q["type"], ["mcq4", "mcq5", "multi", "fill", "tf"])
            if q["type"] == "multi":
                self.assertIsInstance(q["correctIndices"], list)
                self.assertGreaterEqual(len(q["correctIndices"]), 2)


if __name__ == "__main__":
    unittest.main()
