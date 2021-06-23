"""
Given a positive integer n, find and return the longest distance between any two adjacent 1's in the binary representation of n.
If there are no two adjacent 1's, return 0.

Two 1's are adjacent if there are only 0's separating them (possibly no 0's).
The distance between two 1's is the absolute difference between their bit positions.
For example, the two 1's in "1001" have a distance of 3.
"""


class Solution:
    def binaryGap(self, n: int) -> int:
        max_dist = 0
        temp = 0
        s = [c for c in str(bin(n).replace("0b", ""))]

        if s.count("1") <= 1:
            return 0

        for i in range(len(s)):
            if s[i] == "1":
                temp += 1
                max_dist = max(temp, max_dist)
                temp = 0
            else:
                temp += 1
        return max_dist
