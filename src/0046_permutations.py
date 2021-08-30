from collections import *
from typing import *

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        q = deque()
        q.append([])

        for _ in nums:
            level = len(q)
            for i in range(level):
                node = q.popleft()
                for n in nums:
                    if n not in node:
                        new_element = node + [n]
                        q.append(new_element)

        return q