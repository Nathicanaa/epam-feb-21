"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.
Note that after backspacing an empty text, the text will continue empty.
Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".
    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".
    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".
"""


def backspace_compare(first: str, second: str) -> bool:
    """
    Takes 2 strings and checks by remove_sharps() function are they equal after removing
    some characters, # means backspace
    Args:
        first: some sting
        second: another string
    Returns: True if stings are equal, False otherwise
    """
    return remove_sharps(first) == remove_sharps(second)


def remove_sharps(word: str) -> str:
    """
    Takes a sting and make this sting look like after backspaces
    Based on the stack concept
    Args:
        word: some sting
    Returns: reworked sting without sharps
    """
    stack = []
    for char in word:
        if char != "#":
            stack.append(char)
        elif stack:
            stack.pop()
    return "".join(stack)
