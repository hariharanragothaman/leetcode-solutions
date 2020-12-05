from collections import Counter, defaultdict

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ctr = Counter(s)
        keys = list(ctr.keys())

        # Removing unecessary characters - O(1)
        for k in keys:
            if ctr[k] == 1:
                del ctr[k]

        # If the string is a distinct set
        if not ctr.values():
            return -1

        # Getting the characters who repeat
        candidates = ctr.keys()
        hmap = defaultdict(list)

        for i, char in enumerate(s):
            if char in candidates:
                hmap[char].append(i)

        for k, v in hmap.items():
            hmap[k] = hmap[k][-1] - hmap[k][0]

        hmap = {k: v for k, v in sorted(hmap.items(), key=lambda x: x[1], reverse=True)}
        return list(hmap.values())[0] - 1