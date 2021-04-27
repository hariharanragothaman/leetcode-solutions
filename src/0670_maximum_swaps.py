"""
 Given a non-negative integer, you could swap two digits at most once to get the maximum valued number.
 Return the maximum valued number you could get.

Example 1:

Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.

Example 2:

Input: 9973
Output: 9973
Explanation: No swap.

"""


class Solution:
    def maximumSwap(self, num: int) -> int:

        num_str = str(num)
        num = [int(c) for c in num_str]
        arr = sorted((int(c) for c in num_str), reverse=True)

        arr = ''.join(str(c) for c in arr)
        num = ''.join(str(c) for c in num)

        cnt = 0
        for c in zip(arr, num):
            if c[0] > c[1]:
                break
            cnt += 1

        if cnt == len(num):
            return num

        right_index = num.rindex(c[0], cnt +1)
        num = num[:cnt] + num[right_index] + num[cnt+1:right_index] + num[cnt] + num[right_index +1:]
        return num
    