from collections import defaultdict


class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        alpha = [chr(c) for c in range(ord("a"), ord("z") + 1)]
        hmap = defaultdict(int)
        tmp = 0
        for c in alpha:
            hmap[c] = tmp
            tmp += 1

        first_val = second_val = target_val = ""

        def helper(string):
            res = ""
            for c in string:
                res += str(hmap[c])
            return int(res)

        first_val = helper(firstWord)
        second_val = helper(secondWord)
        target_val = helper(targetWord)

        return (first_val + second_val) == target_val
