"""
Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.
"""

"""
Solution approach:
Check if target is in array - if it's there - return the index
else, do binary_search and return the index you would return it.
"""
from bisect import bisect_left


class Solution:
    def searchInsert(self, nums, target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            return bisect_left(nums, target)


if __name__ == '__main__':
    s = Solution()
    arr = [1, 3, 5, 6]
    target = 2
    op = s.searchInsert(arr, target)
    print(op)
