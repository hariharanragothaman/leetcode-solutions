class Solution:
    def arrangeCoins(self, n: int) -> int:
        tmp = list(range(1, 10**5))

        coins = 0
        i = 0
        while coins <= n:
            coins += tmp[i]
            i += 1

        if coins == n:
            return i
        else:
            return i-1