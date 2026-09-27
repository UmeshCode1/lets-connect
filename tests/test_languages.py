import unittest
from activity_lab.languages import analyze_languages

class TestLanguages(unittest.TestCase):
    def test_language_detection(self):
        files = ["src/main.py", "tests/test_main.py", "README.md", "data.json"]
        res = analyze_languages(files)
        self.assertEqual(res["Python"], 2)
        self.assertEqual(res["Markdown"], 1)
        self.assertEqual(res["JSON"], 1)

if __name__ == "__main__":
    unittest.main()
