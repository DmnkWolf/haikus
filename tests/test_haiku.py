import unittest
from pathlib import Path
import src.haikus.haiku as haiku


TESTDATA_PATH = Path(__file__).parent.absolute() / Path('testdata')


class TestHaikuDetection(unittest.TestCase):

    def test_a_valid_haiku(self):
        potential_haiku = (
            'An old silent pond. '
            'A frog jumps into the pond, '
            'splash! Silence again.'
        )
        result = haiku.is_haiku(potential_haiku)
        self.assertTrue(result, f'{potential_haiku} is actually a valid haiku!')

    def test_a_haiku_with_too_many_syllables_in_total(self):
        potential_haiku = (
            'I don\'t know how to create a Haiku. '
            'That\'s why I use too many Syllables '
            'In every part of this poem.'
        )
        result = haiku.is_haiku(potential_haiku)
        self.assertFalse(result, f'{potential_haiku} should not be valid!')

    def test_a_haiku_with_too_few_syllables_in_total(self):
        potential_haiku = (
            'I don\'t '
            'know how to '
            'write a haiku.'
        )
        result = haiku.is_haiku(potential_haiku)
        self.assertFalse(result, f'{potential_haiku} should not be valid!')
