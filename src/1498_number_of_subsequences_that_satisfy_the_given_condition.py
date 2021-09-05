"""
Given an array of integers nums and an integer target.
Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it is less or equal than target.
Since the answer may be too large, return it modulo 10^9 + 7.

Input: nums = [3,5,6,7], target = 9
Output: 4
Explanation: There are 4 subsequences that satisfy the condition.
[3] -> Min value + max value <= target (3 + 3 <= 9)
[3,5] -> (3 + 5 <= 9)
[3,5,6] -> (3 + 6 <= 9)
[3,6] -> (3 + 6 <= 9)

Input: nums = [3,3,6,8], target = 10
Output: 6
Explanation: There are 6 subsequences that satisfy the condition. (nums can have repeated numbers).
[3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]

Input: nums = [2,3,3,4,6,7], target = 12
Output: 61
Explanation: There are 63 non-empty subsequences, two of them don't satisfy the condition ([6,7], [7]).
Number of valid subsequences (63 - 2 = 61).

Input: nums = [5,2,4,1,7,6,8], target = 16
Output: 127
Explanation: All non-empty subset satisfy the condition (2^7 - 1) = 127
"""

"""
Solution:

The basic fundae here is:

1. The total number of subsequences is 2**n if n is the length of the array
2. We can sort the array and choose elements, of min and max - so the order of the elements don't matter
3. This problem is similar to 2-sum - so we have to just pick the min and max elements.
4. Take a look at example-3 - once we find the point of infection we don't need to consider elements after that.
   These are the core crux points
"""

from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0

        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] + nums[right] <= target:
                count += 2 ** (right - left)
                left += 1
            else:
                right = right - 1

        return count % (10 ** 9 + 7)
