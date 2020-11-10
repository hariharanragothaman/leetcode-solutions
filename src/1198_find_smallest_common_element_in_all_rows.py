"""
Given a matrix mat where every row is sorted in strictly increasing order, return the smallest common element in all rows.
If there is no common element, return -1.

Example 1:

Input: mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
Output: 5
"""

from bisect import bisect_left, bisect_right


class Solution:
    def binary_search(self, array, val):
        index = bisect_left(array, val)
        if index != len(array) and array[index] == val:
            return index
        else:
            return -1

    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        values = mat[0]
        mat.pop(0)

        for i, val in enumerate(values):
            # print("Checking if value exists in all", val)
            flag = True
            # Binary Search Recipe
            for arr in mat:
                idx = self.binary_search(arr, val)
                if idx == -1:
                    flag = False
                    break
            if flag:
                return val

        return -1