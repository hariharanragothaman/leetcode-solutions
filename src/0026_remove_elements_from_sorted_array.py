"""
Given a sorted array, remove the duplicates from sorted array
Remove the elements in-place
"""
# Basic things to remember here - use while instead of for  and use the 'del' operator.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                del nums[i]
            else:
                i += 1
        return len(nums)