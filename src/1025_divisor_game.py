class Solution:
    def divisorGame(self, N: int) -> bool:
        if N <= 1:
            return False
        if N % 2 == 0:
            return True
        return False
