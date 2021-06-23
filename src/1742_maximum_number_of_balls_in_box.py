from collections import defaultdict


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        g = defaultdict(int)
        while lowLimit <= highLimit:
            s = sum(int(c) for c in str(lowLimit))
            g[s] += 1
            lowLimit += 1

        g = {k: v for k, v in sorted(g.items(), key=lambda x: x[1], reverse=True)}
        return list(g.values())[0]
