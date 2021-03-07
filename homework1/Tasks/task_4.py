"""
Classic task, a kind of walnut for you
Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    """
    Required that all lists are not empty and have the same length of N where 0 ≤ N ≤ 1000.
    Based on C++ solution at StackOverFlow :
    https://stackoverflow.com/questions/40575323/sum-of-4-integers-in-4-arrays
    Args:
        a: list of ints
        b: list of ints
        c: list of ints
        d: list of ints

    Returns: count of all tuples (i, j, k, l) there are such that a[i] + b[j] + c[k] + d[l] = 0
    """
    dct = {}
    cnt = 0

    for i in range(len(a)):
        for j in range(len(b)):
            x = a[i] + b[j]
            if x not in dct:
                dct[x] = 1
            else:
                dct[x] += 1

    for k in range(len(c)):
        for r in range(len(d)):
            y = c[k] + d[r]
            if -y in dct:
                cnt += dct[-y]

    return cnt
