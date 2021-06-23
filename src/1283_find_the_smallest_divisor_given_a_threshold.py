
from typing import List

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        div_cand = list(range(1, max(nums) + 1))
        left, right = 0, len(div_cand)

        while left < right:
            pivot = (left + right) // 2
            p_div = div_cand[pivot]
            temp = [math.ceil(c / p_div) for c in nums]
            temp_result = sum(temp)

            if temp_result > threshold:
                left = pivot + 1
            elif temp_result <= threshold:
                right = pivot

        return div_cand[right]
