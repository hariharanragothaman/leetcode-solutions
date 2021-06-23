"""
Given a binary string s (a string consisting only of '0's and '1's), we can split s into 3 non-empty strings s1, s2, s3 (s1+ s2+ s3 = s).
Return the number of ways s can be split such that the number of characters '1' is the same in s1, s2, and s3.
Since the answer may be too large, return it modulo 10^9 + 7.
"""

"""
Solution Approach:

Since the given input string will contain only 0's and 1's and we have to split the string into parts containing equals 1's aka equal sum.

- Sanity and corner cases:
1. If total sum is not divisible by 3 - then number of ways is zero
2. What if the string contains only zero'es?
   
   In this scenario - to cut the string into equal sum - its (n-1) cuts.
   To arrange it the prefix and suffix - it be (n-2) waus
   Hence (n-1) * (n-2) // 2

a. Count the number of 1's
b. ones_count = ones_count_total //3 - each part should contain this much
c. Figure out when we have found a prefix, and when we have found a suffix.
   prefix_count, suffix_count = 0, 0

Parse the string and keep counting the 1's
If the count is == to ones_count_total // 3 then we have a prefix
if the count is == ((ones_count_total) // 3 ) * 2 - then only suffix is remaining - we have found a suffix.

"""


class Solution:
    def num_ways(self, s: str) -> int:
        if s.count("1") % 3 == 0:
            return 0

        n = len(s)
        total_ones_count = s.count("1")  # This is also the total sum

        ones_split_count = total_ones_count // 3
        prefix_count, suffix_count = 0, 0
        count = 0

        if total_ones_count == 0:
            return (n - 1) * (n - 2) // 2 % (10 ** 9 + 7)

        for char in s:
            if char == "1":
                count += 1
            if count == ones_split_count:
                prefix_count += 1
            elif count == 2 * ones_split_count:
                suffix_count += 1

            return prefix_count * suffix_count % (10 ** 9 + 7)
