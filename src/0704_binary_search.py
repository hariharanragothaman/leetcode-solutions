"""
Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums.
If target exists, then return its index, otherwise return -1.
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        # Solution using bisect_left
        index = bisect_left(nums, target)
        if index != len(nums) and nums[index] == target:
            return index
        return -1
        """

        # Binary Search Recipe
        left, right = 0, len(nums)
        while left < right:
            pivot = (left + right) // 2
            if nums[pivot] == target:
                return pivot
            elif nums[pivot] < target:
                left = pivot + 1
            else:
                right = pivot

        return -1
