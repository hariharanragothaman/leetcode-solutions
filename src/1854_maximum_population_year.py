from typing import List
from collections import defaultdict
import heapq

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        hmap = defaultdict(int)
        for b, d in logs:
            for i in range(b, d):
                hmap[i] += 1
        mx = heapq.nlargest(1, list(hmap.values()))[0]
        candidates = [k for k, v in hmap.items() if v==mx]
        return sorted(candidates)[0]