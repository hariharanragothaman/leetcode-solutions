from typing import *
from collections import *


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        ctr = Counter()
        e = len(edges)

        for u, v in edges:
            ctr[u] += 1
            ctr[v] += 1

        for k, v in ctr.items():
            if v == e:
                return k
