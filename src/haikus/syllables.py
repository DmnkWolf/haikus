"""
This module helps to count syllables in (english) words.
"""
import re
from pathlib import Path

SYLLABLES_PATTERN = re.compile('[aiouy]+e*|e(?!d$|ly).|[td]ed|le$')
CURRENT_PATH = Path(__file__).parent.absolute()


def _load_dict():
    result = {}
    with open(str(CURRENT_PATH / Path('syllables.txt'))) as syllable_file:
        for word in syllable_file.readlines():
            entry = word.split('=')
            print(entry)
            result[entry[0]] = int(entry[1].replace("\n", ""))
    return result


ALL_WORDS = _load_dict()


def _backup_method(word):
    return len(SYLLABLES_PATTERN.findall(word))


def get_syllables(word):
    """returns the (guessed) number of syllables in a word.

    Args:
        word (string): word to be counted

    Returns:
        int: number of syllables in the word
    """
    if word in ALL_WORDS:
        return ALL_WORDS[word]
    return _backup_method(word)
