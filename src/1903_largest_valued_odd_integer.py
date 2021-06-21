class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        for i in range(n-1, -1, -1):
            if int(num[i]) & 1:
                return num[:i+1]
        return ""


if __name__ == '__main__':
    obj = Solution()
    n = input()
    result = obj.largestOddNumber(n)
    print(f"The result is: {result}")