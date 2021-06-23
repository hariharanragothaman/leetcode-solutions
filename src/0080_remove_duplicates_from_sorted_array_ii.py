"""
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array; you must do this by modifying the input array in-place with O(1) extra memory.

Clarification:

Confused why the returned value is an integer, but your answer is an array?

Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller.
"""
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dup_count = 0
        i = len(nums) - 1

        while i > 0 and nums:
            if nums[i] == nums[i - 1]:
                dup_count += 1
                if dup_count >= 2:
                    dup_count -= 1
                    del nums[i]
            elif nums[i] != nums[i - 1]:
                dup_count = 0

            i -= 1
        return len(nums)