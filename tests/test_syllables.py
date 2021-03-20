import unittest
from pathlib import Path
import src.haikus.syllables as syllables


TESTDATA_PATH = Path(__file__).parent.absolute() / Path('testdata')


class TestSyllableDetection(unittest.TestCase):

    test_cases = {
        'racism': 2,
        'prevaricate': 4,
        'resource': 2
    }

    def test_get_syllables_one_sylable_words(self):
        with open(str(TESTDATA_PATH / Path('1-syllable-words.txt'))) as syllable_file:
            for word in syllable_file.readlines():
                self.assertEqual(syllables.get_syllables(word.replace("\n", "")), 1, f"Wrong syllable count for word {word}")

    def test_get_syllables_two_sylable_words(self):
        with open(str(TESTDATA_PATH / Path('2-syllable-words.txt'))) as syllable_file:
            for word in syllable_file.readlines():
                self.assertEqual(syllables.get_syllables(word.replace("\n", "")), 2, f"Wrong syllable count for word {word}")

    def test_get_syllables_three_sylable_words(self):
        with open(str(TESTDATA_PATH / Path('3-syllable-words.txt'))) as syllable_file:
            for word in syllable_file.readlines():
                self.assertEqual(syllables.get_syllables(word.replace("\n", "")), 3, f"Wrong syllable count for word {word}")

    def test_get_syllables_four_sylable_words(self):
        with open(str(TESTDATA_PATH / Path('4-syllable-words.txt'))) as syllable_file:
            for word in syllable_file.readlines():
                self.assertEqual(syllables.get_syllables(word.replace("\n", "")), 4, f"Wrong syllable count for word {word}")

    def test_get_syllables_five_sylable_words(self):
        with open(str(TESTDATA_PATH / Path('5-syllable-words.txt'))) as syllable_file:
            for word in syllable_file.readlines():
                self.assertEqual(syllables.get_syllables(word.replace("\n", "")), 5, f"Wrong syllable count for word {word}")

    def test_get_syllables_six_sylable_words(self):
        with open(str(TESTDATA_PATH / Path('6-syllable-words.txt'))) as syllable_file:
            for word in syllable_file.readlines():
                self.assertEqual(syllables.get_syllables(word.replace("\n", "")), 6, f"Wrong syllable count for word {word}")

    def test_get_syllables_seven_sylable_words(self):
        with open(str(TESTDATA_PATH / Path('7-syllable-words.txt'))) as syllable_file:
            for word in syllable_file.readlines():
                self.assertEqual(syllables.get_syllables(word.replace("\n", "")), 7, f"Wrong syllable count for word {word}")