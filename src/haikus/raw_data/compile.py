from pathlib import Path


DATA_PATH = Path(__file__).parent.absolute()
TARGET_PATH = Path(__file__).parent.parent.absolute() / Path('syllables.txt')


def _add_from_testfile(file_name, syllable_count, complete_dict):
    with open(str(DATA_PATH / Path(file_name)), encoding='utf-8') as test_file:
        for word in test_file.readlines():
            word = word.replace("\n", "")
            if not word in complete_dict:
                complete_dict[word] = syllable_count
    return complete_dict


def _load_data():
    compl_dict = _load_dict()
    compl_dict = _add_from_testfile('1-syllable-words.txt', 1, compl_dict)
    compl_dict = _add_from_testfile('2-syllable-words.txt', 2, compl_dict)
    compl_dict = _add_from_testfile('3-syllable-words.txt', 3, compl_dict)
    compl_dict = _add_from_testfile('4-syllable-words.txt', 4, compl_dict)
    compl_dict = _add_from_testfile('5-syllable-words.txt', 5, compl_dict)
    compl_dict = _add_from_testfile('6-syllable-words.txt', 6, compl_dict)
    compl_dict = _add_from_testfile('7-syllable-words.txt', 7, compl_dict)
    return compl_dict


def _load_dict():
    result = {}
    syl_path = str(DATA_PATH / Path('syllables.txt'))
    with open(syl_path, encoding='utf-8') as syllable_file:
        for entry in syllable_file.readlines():
            word, syllables = entry.split('=')
            if not word in result:
                result[word] = syllables.count('·') + 1
    return result


def _compile():
    complete_dict = _load_data()
    with open(str(TARGET_PATH), "w") as output_file:
        for word in complete_dict:
            output_file.write(f"{word}={complete_dict[word]}\n")


_compile()
