from typing import List
from collections import Counter

# Remmeber Counter() remembers the order

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        hashmap = Counter()
        hashmap[0] = 1
        count = 0

        for i in range(1, n + 1):
            value = prefix_sum[i - 1] + nums[i - 1]
            prefix_sum[i] = value
            count += hashmap.get(value - k, 0)
            hashmap[value] += 1

        return count
