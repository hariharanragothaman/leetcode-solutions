"""
You are given a string time in the form of hh:mm, where some of the digits in the string are hidden (represented by ?).

The valid times are those inclusively between 00:00 and 23:59.

Return the latest valid time you can get from time by replacing the hidden digits.



Example 1:

Input: time = "2?:?0"
Output: "23:50"
Explanation: The latest hour beginning with the digit '2' is 23 and the latest minute ending with the digit '0' is 50.
Example 2:

Input: time = "0?:3?"
Output: "09:39"
Example 3:

Input: time = "1?:22"
Output: "19:22"


Constraints:

time is in the format hh:mm.
It is guaranteed that you can produce a valid time from the given string.
"""


class Solution:
    def maximumTime(self, time: str) -> str:
        _h1 = ['1', '2']
        _h2 = {'0': '9', '1': '9', '2': '3'}
        _m1 = ['5']
        _m2 = {'0': '9', '1': '9', '2': '9', '3': '9', '4': '9', '5': '9'}

        h, m = time.split(':')

        h1, h2 = [c for c in h]
        m1, m2 = [c for c in m]

        print(h1, h2)
        print(m1, m2)

        if h1 == '?' and h2 != '?' and int(h2) < 4:
            h1 = _h1[1]
        if h1 == '?' and h2 != '?' and int(h2) >= 4:
            h1 = _h1[0]
        if h1 == '?' and h2 == '?':
            h1 = _h1[1]
        if h2 == '?':
            h2 = _h2[h1]
        if m1 == '?':
            m1 = _m1[0]
        if m2 == '?':
            m2 = _m2[m1]

        return h1 + h2 + ':' + m1 + m2
