class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        opened = ['(']
        closed = [')']

        s = [c for c in s]
        print(s)

        stack = []
        to_remove = set()
        for i in range(len(s)):
            if s[i] in opened:
                stack.append((s[i],i))
            elif s[i] in closed:
                print("The stack is:",stack)
                if stack and stack[-1][0] in opened:
                    stack.pop()
                elif stack and stack[-1][0] not in opened:
                    print("Entering here...")
                    to_remove.add(i)
                else:
                    stack.append((s[i], i))

        if stack:
            for c, idx in stack:
                to_remove.add(idx)
        print(f"The to_remove array is:", to_remove)

        result = ''
        for i, val in enumerate(s):
            if i not in to_remove:
                result += val

        return result


if __name__ == '__main__':
    obj = Solution()
    s = input()
    result = obj.minRemoveToMakeValid(s)
    print(f"The result is: {result}")