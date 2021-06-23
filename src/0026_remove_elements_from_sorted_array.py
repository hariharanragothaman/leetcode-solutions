"""
Given a sorted array, remove the duplicates from sorted array
Remove the elements in-place
"""
# Basic things to remember here - use while instead of for  and use the 'del' operator.

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                del nums[i]
            else:
                i += 1
        return len(nums)

    def removeDuplicatesUpdated(self, nums: List[int]) -> int:
        # Solution by over-writing
        write_index = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[write_index - 1]:
                nums[write_index] = nums[i]
                write_index += 1
        return write_index
