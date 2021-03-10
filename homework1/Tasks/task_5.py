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
    Finds a sub-array with length less or equal to "k", with maximal sum.
    Args:
        nums: list of int numbers
        k: max length of sub-array

    Returns: max sum of sub-array with length <= k
    """
    current_start = 0
    best_sum = 0
    current_sum = None

    if not nums or k <= 0:
        return best_sum

    for i in range(len(nums)):

        if current_sum is None:
            best_sum = nums[i]
            current_sum = nums[i]
            current_start = i

        elif nums[i] > current_sum + nums[i]:
            current_sum = nums[i]
            current_start = i

        else:
            current_sum += nums[i]

        if i - current_start == k:
            current_sum -= nums[i - k]
            current_start += 1

        if current_sum > best_sum:
            best_sum = current_sum

    return best_sum
