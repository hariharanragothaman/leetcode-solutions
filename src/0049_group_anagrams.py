from typing import *
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for word in strs:
            s = ''.join(sorted(word))
            hashmap[s].append(word)
        return list(hashmap.values())