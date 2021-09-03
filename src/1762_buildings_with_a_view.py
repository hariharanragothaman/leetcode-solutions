from typing import *

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        minx = heights[-1]
        res = [n-1]
        for i in range(n-2, -1, -1):
            if heights[i] > minx:
                minx = heights[i]
                res.append(i)
        res = res[::-1]
        return res