"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.
For dir with two files from hw1.py:
>> universal_file_counter(test_dir, "txt")
6
>> universal_file_counter(test_dir, "txt", str.split)
6
"""
from pathlib import Path
from typing import Callable, Generator, Optional


def yield_line(dir_path: Path, file_extension: str) -> Generator:
    """
    Takes directory path and a file extension and finds all files with
    this extension in given directory, then reads files and yields line by line
    Args:
        dir_path: some directory
        file_extension: some file extension
    Yields: line from a file in given directory
    """
    for file in dir_path.glob("*." + file_extension):
        with open(file, encoding="utf-8") as fi:
            yield from fi


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    """
    Takes directory path, file extension and optionality tokenizer
    If tokenizer is not none then counting tokens in directory files
    otherwise function will just count whole lines in these files
    Args:
        dir_path: some directory
        file_extension: some file extension
        tokenizer: some callable object
    Returns: count of token or lines
    """
    cnt = 0
    for line in yield_line(dir_path, file_extension):
        if tokenizer:
            cnt += sum(1 for _ in (tokenizer(line)))
        else:
            cnt += 1
    return cnt
