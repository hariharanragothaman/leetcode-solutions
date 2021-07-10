from typing import *

class Solution:
    def countTriples(self, n: int) -> int:
        # So to count pythogorean triplets until n
        cnt = 0
        for i in range(1, n):
            for j in range(i+1, n):
                c = (i**2 + j**2) ** 0.5
                if 1 <= c <= n and c.is_integer():
                    cnt += 2
        return cnt