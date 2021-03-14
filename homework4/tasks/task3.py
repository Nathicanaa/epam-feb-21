"""
Write a function that will receive a string and write it to stderr
if line starts with "error" and to the stdout otherwise.
my_precious_logger("error: file not found")
# stderr
'error: file not found'
my_precious_logger("OK")
# stdout
'OK'
Definition of done:
 - function is created
 - function is properly formatted
 - function has positive tests
You will learn:
 - how to write to stderr
 - how to test output to the stderr and stdout
"""
import sys


def my_precious_logger(text: str) -> None:
    """
    Takes text, if text starts with 'error' puts this text to stderr
    otherwise it puts to stdout
    Args:
        text: some text

    Returns: func doesn't return anything, just prints in stdout/stderr

    """
    if text.startswith("error"):
        print(text, file=sys.stderr)
    else:
        print(text, file=sys.stdout)
