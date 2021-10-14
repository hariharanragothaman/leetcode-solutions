from collections import defaultdict
from typing import *

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:

        # Store the hashmap and count the k - apart counts
        hashmap = defaultdict(int)
        count = 0

        # Creating a count map
        for c in nums:
            hashmap[c] += 1

        for num in range(k, 101):
            diff = num - k
            count += hashmap[num] * hashmap[diff]

        return count