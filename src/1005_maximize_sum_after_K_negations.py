"""
Given an array A of integers, we must modify the array in the following way: we choose an i and replace A[i] with -A[i], and we repeat this process K times in total.  (We may choose the same index i multiple times.)
Return the largest possible sum of the array after modifying it in this way.

"""
from typing import List


class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort()
        i = 0
        # Pick all negative numbers and flip them
        while i < len(A) and K > 0 and A[i] < 0:
            A[i] = A[i] * -1
            i += 1
            K -= 1

        # now, that we have attacked all negative numbers - we need to head to positive numbers
        # The crucial part to remember here - is when we start to think about flipping the positive.
        # consider the minimum value in the array now, as some of the negative numbers have become postive.
        min_value = min(A)
        if K % 2 != 0:
            idx = A.index(min_value)
            A[idx] = A[idx] * -1

        return sum(A)