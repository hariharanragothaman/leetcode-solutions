from typing import List

class Solution:
    def lastStoneWeight(self, nums: List[int]) -> int:
        if not nums:
            return 0

        elif len(nums) == 1:
            return nums[0]

        elif len(nums) == 2:
            return abs(nums[0] - nums[1])

        else:
            max1 = max(nums)
            nums.remove(max1)
            max2 = max(nums)
            nums.remove(max2)

            if max1 != max2:
                val = abs(max1 - max2)
                nums.append(val)

        val = self.lastStoneWeight(nums)
        return val