"""
Module to handle haikus
"""
import re
from .syllables import get_syllables


CLEANING_PATTERN = re.compile(r'[^\w]')


def is_haiku(haiku: str) -> bool:
    """tells you if the string is a haiku.

    Args:
        haiku (str): text of the potential haiku

    Returns:
        bool: true if it is a haiku, false if not
    """
    words = [CLEANING_PATTERN.sub('', word) for word in haiku.split(' ')]
    syllable_counts = [get_syllables(word) for word in words]
    syllable_count = sum(syllable_counts)
    return syllable_count == 17
