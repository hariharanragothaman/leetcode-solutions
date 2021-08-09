class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        """
        As long as a prefix == rev(bsuffix) keep forming the split
        do this (a, b) and (b, a)
        if any of them are palindromes, then it's true
        """
        i = 0
        j = len(a) -1

        while i < j and a[i] == b[j]:
            i = i + 1
            j = j - 1
        s1 = a[i:j+1]
        s2 = b[i:j+1]

        print(s1, s2)

        i, j = 0, len(a) - 1
        while i < j and b[i] == a[j]:
            i, j = i + 1, j - 1
        s3, s4 = a[i:j + 1], b[i:j + 1]
        print(s3, s4)

        return any(s == s[::-1] for s in (s1,s2,s3,s4))