from typing import List
from collections import Counter


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        nums = sorted(nums, key=lambda x: (freq[x], -x))
        return nums
