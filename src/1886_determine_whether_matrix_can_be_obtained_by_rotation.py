from typing import List

class Solution:
    def rotate(self, mat):
        mat[:] = zip(*mat[::-1])
        return mat

    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        # Converting it into a tuple
        target = [tuple(c) for c in target]
        print("The target is:", target)

        # We need to check if mat can be made into target by rotating
        # Starting to rotate mat

        for i in range(4):
            result = self.rotate(mat)
            print(result)
            if result == target:
                return True
        return False