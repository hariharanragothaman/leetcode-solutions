class Solution:
    def twoSum(self, nums, target):
        """
        This basically return all possible
        indexes of numbers that can add to a number
        """
        hmap = {}
        result = []
        for i, n in enumerate(nums):
            hmap[n] = i

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hmap and hmap[diff] != i:
                result.append(sorted((i, hmap[diff])))
        return result

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result, sol = [], []
        target = 0

        for j, a in enumerate(nums):
            idx = self.twoSum(nums, target - a)
            fdx = []
            [fdx.append(c) for c in idx if c not in fdx]
            for tup in fdx:
                if j not in tup:
                    sol = sorted([a, nums[tup[0]], nums[tup[1]]])
                if sol and sol not in result:
                    result.append(sol)
        return result