from typing import *


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        # Calculating prefix-sum
        prefix_sum = [0] * n
        prefix_sum[0] = nums[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]

        hashmap = {0: -1}
        for i in range(len(prefix_sum)):
            if k == 0:
                remainder = prefix_sum[i]
            else:
                remainder = prefix_sum[i] % k

            if remainder in hashmap:
                if i - hashmap[remainder] > 1:
                    return True
            else:
                hashmap[remainder] = i
        return False
