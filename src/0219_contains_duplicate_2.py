"""
Given an integer array nums and an integer k,
return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
"""

from typing import *

def contains_nearby_duplicate(nums: List[int], k):
    hashmap = {}
    for i, c in enumerate(nums):
        if c not in d:
            hashmap[c] = [i]
        else:
            for n in hashmap[c]:
                if abs(n-i) <= k:
                    return True
            hashmap[c].append(i)
    return False