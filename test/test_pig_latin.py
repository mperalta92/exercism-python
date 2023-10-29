import unittest
from pig_latin import translate


class TestPigLatin(unittest.TestCase):

    def test_pig_latin_word_begining_with_thr(self):
        self.assertEqual(translate("three"), "eethray")
        self.assertEqual(translate("thrush"), "ushthray")

    def test_pig_latin_a_whole_phrase(self):
        self.assertEqual(translate("quick fast run"), "ickquay astfay unray")
