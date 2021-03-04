"""
Given a list of integers numbers "nums".
You need to find a sub-array with length less equal to "k", with maximal sum.
The written function should return the sum of this sub-array.
Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    """
    Find subarray with the largest sum that has length k.
    Based on Kadane's algorithm. Nums array shouldn't be empty and k must be > 0
    otherwise it will return -1
    """
    best_sum = float("-inf")
    current_sum = 0

    if not nums or k <= 0:
        return -1

    for current_end, x in enumerate(nums):

        if current_sum <= 0:
            current_sum = x
            current_start = current_end
        else:
            current_sum += x

        if current_end - current_start == k:
            current_sum -= nums[current_start]
            current_start += 1

        if current_sum > best_sum:
            best_sum = current_sum

    return best_sum
