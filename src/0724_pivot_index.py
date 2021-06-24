from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = [0] * (n+1)
        for i in range(1, n+1):
            prefix_sum[i] = prefix_sum[i-1] + nums[i-1]

        for i in range(1, n+1):
            left_sum = prefix_sum[i-1]
            right_sum = prefix_sum[-1] - prefix_sum[i]
            if left_sum == right_sum:
                return i -1
        return -1