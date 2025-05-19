
from dataclasses import dataclass
import unittest

@dataclass
class WordPatternProblem:
    def solve(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for i in range(len(pattern)):
            p = pattern[i]
            w = words[i]
            if p in char_to_word:
                if char_to_word[p] != w:
                    return False
            else:
                if w in word_to_char:
                    return False
                char_to_word[p] = w
                word_to_char[w] = p

        return True

class TestWordPatternProblem(unittest.TestCase):
    def setUp(self):
        self.word_pattern = WordPatternProblem()

    def test_example(self):
        self.assertTrue(self.word_pattern.solve("abba", "dog cat cat dog"))

    def test_false_c(self):
        self.assertFalse(self.word_pattern.solve("abba", "dog cat cat fish"))

    def test_false_c2(self):
        self.assertFalse(self.word_pattern.solve("aaaa", "dog cat cat dog"))

    def test_lengths(self):
        self.assertFalse(self.word_pattern.solve("abc", "dog cat"))

    def test_different(self):
        self.assertTrue(self.word_pattern.solve("abc", "dog cat fish"))

    def test_false_pattern(self):
        self.assertFalse(self.word_pattern.solve("abc", "dog dog dog"))

    def test_empty(self):
        self.assertTrue(self.word_pattern.solve("", ""))

    def test_non_empty_s(self):
        self.assertFalse(self.word_pattern.solve("", "dog"))

    def test_non_empty_pattern(self):
        self.assertFalse(self.word_pattern.solve("a", ""))

    def test_single_letter(self):
        self.assertTrue(self.word_pattern.solve("a", "dog"))

if __name__ == "__main__":
    unittest.main()
