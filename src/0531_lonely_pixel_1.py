from typing import *


class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        R = len(picture)
        C = len(picture[0])

        # To get the rows of the matrix:
        def get_rows(matrice):
            return [[c for c in r] for r in matrice]

        # To the cols of the matrix
        def get_columns(matrice):
            return zip(*matrice)

        candidates = []

        for i in range(R):
            for j in range(C):
                if picture[i][j] == "B":
                    candidates.append((i, j))

        # print(f"The candidates are: {candidates}")

        rows = []
        cols = []

        for r in get_rows(picture):
            rows.append(r)

        for c in get_columns(picture):
            cols.append(c)

        # print(f"The rows are: {rows}")
        # print(f"The cols are: {cols}")

        cnt = 0

        for i, j in candidates:
            # print(i, j, rows[i], cols[j])
            if rows[i].count("B") == 1 and cols[j].count("B") == 1:
                cnt += 1

        return cnt
