"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import string
from collections import Counter
from typing import List


def get_text(file_path: str, encoding: str = "unicode_escape") -> str:
    """
    A Func reads data from file
    Args:
        file_path: a path to the file with data
        encoding: default encoding is unicode_escape

    Returns: str data from file

    """
    with open(file_path, encoding=encoding) as fi:

        return fi.read()


def get_longest_diverse_words(file_path: str) -> List[str]:
    """
    Find 10 longest unique words in file
    Args:
        file_path: a path to the file with data

    Returns: list of 10 longest words consisting from largest amount of unique symbols

    """
    text = get_text(file_path)

    if "-\n" in text:
        text = text.replace("-\n", "")

    for sym in string.punctuation:
        text = text.replace(sym, "")

    words = {word: len(set(word)) for word in text.split()}
    counts = sorted(words.items(), key=lambda x: x[1], reverse=True)

    return [pair[0] for pair in counts[0:10]]


def get_rarest_char(file_path: str) -> str:
    """
    Find the rarest char in file
    Args:
        file_path: a path to the file with data

    Returns: rarest char in file

    """
    text = get_text(file_path)
    chars = {}
    for line in text:
        for char in line:
            if char not in chars:
                chars[char] = 1
            else:
                chars[char] += 1

    return [key for key, value in chars.items() if value == min(chars.values())][0]


def count_punctuation_chars(file_path: str) -> int:
    """
    Find count of all punctuation chars in the file
    Args:
        file_path: a path to the file with data

    Returns: int count of all punctuation chars in the file

    """
    text = get_text(file_path)
    cnt_punctuation = 0

    for line in text:
        for char in line:
            if char in string.punctuation:
                cnt_punctuation += 1

    return cnt_punctuation


def count_non_ascii_chars(file_path: str) -> int:
    """
    Find count of all non-ascii chars in the file
    Args:
        file_path: a path to the file with data

    Returns: int count of all non-ascii chars in the file

    """
    text = get_text(file_path)
    cnt_non_ascii = 0

    for line in text:
        for char in line:
            if not char.isascii():
                cnt_non_ascii += 1

    return cnt_non_ascii


def get_most_common_non_ascii_char(file_path: str) -> str:
    """
    Find most common non ascii char in the file
    Args:
        file_path: a path to the file with data

    Returns: most common non ascii char in the file

    """
    text = get_text(file_path)
    counted = Counter(text).most_common()

    for pair in counted:
        if not pair[0].isascii():

            return pair[0]
