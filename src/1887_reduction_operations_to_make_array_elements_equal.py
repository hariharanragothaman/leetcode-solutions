from typing import List


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        # Think of how many numbers are after a specific number
        # Get the right most occurance
        nums.sort()
        cnt = 0
        n = len(nums)
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                cnt += n - i
        return cnt
