from collections import deque


class Solution:
    def decodeString(self, s):
        s1, s2 = [], []
        s = [c for c in s]
        q = deque(s)
        alpha = [chr(c) for c in range(ord("a"), ord("z") + 1)]
        open, close = ["["], ["]"]
        prev_digit = False

        while q:
            node = q.popleft()
            if node.isdigit() and prev_digit:
                s1[-1] = s1[-1] + node
                prev_digit = True

            elif node.isdigit():
                s1.append(node)
                prev_digit = True

            elif node in alpha or node in open:
                s2.append(node)
                prev_digit = False

            elif node in close:
                tmp = []
                while s2:
                    char = s2.pop()
                    if char in open:
                        tmp = tmp[::-1]
                        break
                    else:
                        tmp.append(char)
                mul = s1.pop()
                s2 += tmp * int(mul)
        return "".join(s2)


if __name__ == "__main__":
    s = "3[a10[c]]"
    obj = Solution()
    ans = obj.decodeString(s)
    print(ans)
