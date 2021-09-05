from typing import *


class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        R = len(mat)
        C = len(mat[0])

        def neighbours(r, c, R, C):
            for rows, cols in (
                (r - 1, c),
                (r, c - 1),
                (r + 1, c),
                (r, c + 1),
                (r + 1, c + 1),
                (r - 1, c - 1),
                (r - 1, c + 1),
                (r + 1, c - 1),
            ):
                if 0 <= rows < R and 0 <= cols < C:
                    yield rows, cols

        DP = [[0] * C for i in range(R)]

        for i in range(R):
            for j in range(C):
                if mat[i][j] == 1:
                    for nr, nc in neighbours(i, j, R, C):
                        if mat[nr][nc] == 1:
                            DP[i][j] += 1
        print(DP)


if __name__ == "__main__":
    s = Solution()
    mat = [[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 1]]
    s.longestLine(mat)
