from typing import *


class SparseVector:
    def __init__(self, nums: List[int]):
        self.v1 = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: "SparseVector") -> int:
        self.ans = 0
        for c in zip(self.v1, vec.v1):
            if c[0] != 0 and c[1] != 0:
                self.ans += c[0] * c[1]
        return self.ans


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
