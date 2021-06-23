from typing import List
from operator import xor
import itertools


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def xor_total(arr):
            res = list(itertools.accumulate(arr, xor))
            return res[-1]

        n = len(nums)
        s = 0
        for i in range(n + 1):
            for c in itertools.combinations(nums, i):
                if c:
                    s += xor_total(c)
        return s
