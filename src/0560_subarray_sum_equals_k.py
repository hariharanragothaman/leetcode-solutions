from typing import List
from collections import Counter

# Remmeber Counter() remembers the order


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        n = len(nums)
        prefix_sum = [0] * (n + 1)

        # Get the prefix sum
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]

        ctr = Counter()
        ctr[0] = 1
        ans = 0

        for i in range(1, len(prefix_sum)):
            ans += ctr.get(prefix_sum[i] - k, 0)
            ctr[prefix_sum[i]] += 1
        return ans
