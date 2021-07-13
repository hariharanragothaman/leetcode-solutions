from typing import *
from collections import *

class Solution:
    def longestAwesome(self, s: str) -> int:
        """
        So essentially we need to find the longest substring, that satisfies these conditions
        1. Which does not have more than one number have an odd-count (frequency) - Basic condition
        2. Now coming to even-length, and odd-length
            a. It's odd-length - then except for odd count character, every other character freq_count // 2 + odd_cnt + reverse[]
            b, It's even-length - then every character, freq // 2 + reverse it?
        """

        # So we are moving right, and reducing length by 1
        # for every time we move right - we start from the longest substring that can be formed to lowest one
        # So the moment, we find something we can instantly breal

        max_length = 0

        if s == s[::-1]:
            return len(s)

        for i in range(0, len(s)):
            left = i
            right = len(s)

            if right - left > max_length:

                while right > left:

                    candidate = s[left:right]
                    # print(f"The candidate is: {candidate}")
                    ctr = Counter(candidate)

                    # initial base check
                    odd_cnt = 0
                    fl = False
                    for k, v in ctr.items():
                        if v & 1:
                            odd_cnt += 1
                        if odd_cnt > 1:
                            fl = True
                            break

                    if not fl:
                        if max_length < (right - left):
                            max_length = right - left
                            # max_length = max(max_length, len(candidate))

                    right -= 1

        return max_length