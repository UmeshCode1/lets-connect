import unittest
from activity_lab.git_attributes import parse_gitattributes

class TestGitAttributes(unittest.TestCase):
    def test_parse(self):
        text = "* text=auto\n*.py text eol=lf"
        res = parse_gitattributes(text)
        self.assertEqual(res["*"]["text"], "auto")
        self.assertEqual(res["*.py"]["eol"], "lf")

if __name__ == "__main__":
    unittest.main()
