"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]

"""


class Solution:
    def generateParenthesis(self, n):
        res = []
        s = [("(", 1, 0)]
        while s:
            x, l, r = s.pop()
            if l - r < 0 or l > n or r > n:
                continue
            if l == n and r == n:
                res.append(x)
            s.append((x + "(", l + 1, r))
            s.append((x + ")", l, r + 1))
        return res


if __name__ == "__main__":
    s = Solution()
    s.generateParanthesis(5)
