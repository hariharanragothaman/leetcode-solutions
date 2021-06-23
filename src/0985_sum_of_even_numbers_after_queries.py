from typing import List

# This solution however TLE's - need to optimize
class Solution:
    def sumEvenAfterQueries(
        self, nums: List[int], queries: List[List[int]]
    ) -> List[int]:
        result = []
        for val, idx in queries:
            nums[idx] += val
            result.append(sum(c for c in nums if not c & 1))
        return result
