"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"
Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"
    [[-, -, o],
     [-, o, o],
     [x, x, x]]
     Return value should be "x wins!"
"""
from typing import Any, List

DRAW = "draw!"
UNFINISHED = "unfinished!"


def win_lines_maker(base_board: List[List]) -> List[Any]:
    """
    Takes 3x3 tic tac toe board and splits it into possible win lines
    Args:
        base_board: 3x3 tic tac toe board
    Returns: list of 8 lines ( 3 horizontal, 3 vertical and 2 diagonal )
    """
    possible_win_lines = [sublist for sublist in base_board]
    [
        possible_win_lines.append(el)
        for el in zip(base_board[0], base_board[1], base_board[2])
    ]
    possible_win_lines.append([base_board[0][0], base_board[1][1], base_board[2][2]])
    possible_win_lines.append([base_board[2][0], base_board[1][1], base_board[0][2]])
    return possible_win_lines


def win_checker(win_lines: List[Any]) -> str:
    """
    Checks for win, draw or unfinished conditions in possible
    win combinations
    Args:
        win_lines: a list containing possible win combinations
    Returns: result of checking win combinations, can be win, draw or unfinished
    """
    flag = False
    for combination in win_lines:
        if combination[0] == combination[1] == combination[2] != "-":
            return combination[0]
        if "-" in combination:
            flag = True
    if flag:
        return UNFINISHED
    return DRAW


def tic_tac_toe_checker(board: List[List]) -> str:
    """
    The main function that takes 3x3 tic tac toe board and then makes a new list
    with possible win combinations, after that checks for a result of the game in
    these combinations
    Args:
        board: 3x3 tic tac toe bord
    Returns: result of the game: win x / win o, draw or unfinished
    """
    lines = win_lines_maker(board)
    result = win_checker(lines)
    if result == DRAW:
        return f"{DRAW}"
    if result == UNFINISHED:
        return f"{UNFINISHED}"
    return f"{result} wins!"
