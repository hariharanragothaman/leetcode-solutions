from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        both_like = [c for c in list1 if c in list2]
        hashmap = {}
        for c in both_like:
            hashmap[c] = list1.index(c) + list2.index(c)
        hashmap = {k:v for k, v in sorted(hashmap.items(), key=lambda x:x[1])}
        mi = min(list(hashmap.values()))
        res = []
        for k, v in hashmap.items():
            if v == mi:
                res.append(k)
        return res