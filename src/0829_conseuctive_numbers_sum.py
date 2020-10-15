"""
Given a positive integer N, how many ways can we write it as a sum of consecutive positive integers?
"""
# This idea is to use a sliding window here
class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        window = list(range(1, N))
        csum, count = 0, 0
        left, right = 0, 0

        while right < len(window):
            csum += window[right]

            while csum > N:
                csum -= window[left]
                left += 1

            if csum == N: count += 1
            right += 1

        return count + 1