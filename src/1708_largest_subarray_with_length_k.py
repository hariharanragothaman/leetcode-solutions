from typing import List


class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        """
        Here the core idea is, we can only form subarray of length starting till len(nums)-k+1
        Since only the first element matters - we only need to start from there
        This is a greedy approach.

        :param nums:
        :param k:
        :return:
        """

        if k == 1: return [max(nums)]

        hash_map = {}
        for i, n in enumerate(nums):
            hash_map[n] = i

        candidates = nums[:len(nums) - k + 1]
        print(candidates)
        mx = max(candidates)
        mx_idx = hash_map[mx]
        op = nums[mx_idx:mx_idx + k]
        return op