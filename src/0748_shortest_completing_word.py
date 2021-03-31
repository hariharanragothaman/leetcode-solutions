from collections import Counter, defaultdict
from typing import List

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlate = ''.join(c.lower() for c in licensePlate if c.isalpha())
        lctr = Counter(licensePlate)
        rmap = defaultdict(list)

        for word in words:
            wordCounter = Counter(word)
            temp = ''.join(c for c in word if c in licensePlate)
            fl = True

            if temp:
                tctr = Counter(temp)
                for k, v in lctr.items():
                    if k not in temp or tctr[k] < v:
                        fl = False
                if fl: rmap[len(word)].append(word)

        rmap = {k: v for k, v in sorted(rmap.items(), key=lambda x: x[0])}
        values = list(rmap.values())
        if values:
            return values[0][0]