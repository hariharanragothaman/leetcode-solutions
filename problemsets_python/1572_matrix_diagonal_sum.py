"""
Given a square matrix mat, return the sum of the matrix diagonals.
Only include the sum of all the elements on the primary diagonal and
all the elements on the secondary diagonal that are not part of the primary diagonal.

Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25

Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
Output: 8

"""

"""
Solution Approach:
Basically since we want to find the sum of left and right diagonals.
For left diagonals  -  (0,0), (1,1), (2,2) -   { i and j are the same }
For right diagonals -  (0,2), (1,1), (2,0) -   { Look at it from reverse -   cols increasing 0-1-2, and rows: 2-1-0}

"""


class Solution:
    def diagonalSum(self, mat) -> int:
        rows = len(mat)
        hashmap = {}

        for i in range(rows):
            hashmap[(i, i)] = mat[i][i]

        for i in range(rows):
            print((rows - 1 - i, i))
            hashmap[(rows - 1 - i, i)] = mat[rows - 1 - i][i]

        return sum(hashmap.values())


if __name__ == "__main__":
    sol = Solution()
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    output = sol.diagonalSum(mat)
    print("The diagonal sum is:", output)
