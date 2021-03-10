"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.
You may assume that the array is non-empty and the most common element
always exist in the array.
Example 1:
Input: [3,2,3]
Output: 3, 2
Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2, 1
"""
from collections import Counter
from typing import List, Tuple


def major_and_minor_elem(inp: List[int]) -> Tuple[int, int]:
    """
    The function returns most common and least common numbers of given list
    list is not empty and most common element always exists
    Args:
        inp: list of integers
    Returns: a tuple with most common and least common element
    """
    cnt = Counter(inp).most_common()
    most_common, most_common_count = cnt[0]

    least_common, least_common_count = cnt.pop()
    list_of_all_counts = list(
        map(lambda x: x[1], cnt)
    )  # need for cases like [1,1,1,2,3] or [1,1,1,1]

    if len(cnt) == 0 or least_common_count in list_of_all_counts:
        raise ValueError("There is no least common element")

    return most_common, least_common
