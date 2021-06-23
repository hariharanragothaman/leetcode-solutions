"""
Given an array of integers A, return the largest integer that only occurs once.

If no integer occurs once, return -1.



Example 1:

Input: [5,7,3,9,4,9,8,3,1]
Output: 8
Explanation:
The maximum integer in the array is 9 but it is repeated. The number 8 occurs only once, so it's the answer.

Example 2:

Input: [9,9,8,8]
Output: -1
Explanation:
There is no number that occurs only once.



Note:

    1 <= A.length <= 2000
    0 <= A[i] <= 1000


"""

from collections import Counter
from typing import List


class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        ctr = Counter(A)
        ctr = {k: v for k, v in ctr.items() if v == 1}
        if ctr:
            ctr = {
                k: v for k, v in sorted(ctr.items(), key=lambda x: x[0], reverse=True)
            }
            return list(ctr.keys())[0]
        else:
            return -1
