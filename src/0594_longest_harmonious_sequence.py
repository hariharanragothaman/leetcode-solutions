"""
We define a harmonious array as an array where the difference between
its maximum value and its minimum value is exactly 1.
Given an integer array nums, return the length of its
longest harmonious subsequence among all its possible subsequences.
A subsequence of array is a sequence that can be derived from the array by
deleting some or no elements without changing the order of the remaining elements.

Solution thoughts:

1. The basic idea is to see if 1+key_value is there in the hashmap and since we are looking for longest - max()

"""

from collections import Counter


def longest_harmonious_sequence(nums):
    ctr = Counter(nums)
    keys = set(ctr.keys())
    # Case 1- There is no sequence
    if len(ctr.keys()) == 1:
        return 0

    max_length = 0
    for k in keys:
        if 1 + k in ctr:
            max_length = max(max_length, ctr.get(k) + ctr.get(1 + k))

    return max_length
