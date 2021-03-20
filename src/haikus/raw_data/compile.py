from pathlib import Path


DATA_PATH = Path(__file__).parent.absolute()
TARGET_PATH = Path(__file__).parent.parent.absolute() / Path('syllables.txt')


def _add_from_testfile(file_name, syllable_count, complete_dict):
    with open(str(DATA_PATH / Path(file_name))) as test_file:
        for word in test_file.readlines():
            word = word.replace("\n", "")
            if not word in complete_dict:
                complete_dict[word] = syllable_count
    return complete_dict


def _load_data():
    complete_dict = _load_dict()
    complete_dict = _add_from_testfile('1-syllable-words.txt', 1, complete_dict)
    complete_dict = _add_from_testfile('2-syllable-words.txt', 2, complete_dict)
    complete_dict = _add_from_testfile('3-syllable-words.txt', 3, complete_dict)
    complete_dict = _add_from_testfile('4-syllable-words.txt', 4, complete_dict)
    complete_dict = _add_from_testfile('5-syllable-words.txt', 5, complete_dict)
    complete_dict = _add_from_testfile('6-syllable-words.txt', 6, complete_dict)
    complete_dict = _add_from_testfile('7-syllable-words.txt', 7, complete_dict)
    return complete_dict


def _load_dict():
    result = {}
    with open(str(DATA_PATH / Path('syllables.txt'))) as syllable_file:
        for word in syllable_file.readlines():
            entry = word.split('=')
            result[entry[0]] = len(entry[1].split('·'))
    return result


def _compile():
    complete_dict = _load_data()
    with open(str(TARGET_PATH), "w") as output_file:
        for word in complete_dict:
            output_file.write(f"{word}={complete_dict[word]}\n")


_compile()
