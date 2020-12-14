class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        i = 0
        output = []

        for c in zip(nums, sorted(nums)):
            if c[0] != c[1]:
                output.append(i)
            i += 1

        if output:
            return max(output) - min(output) + 1
        else:
            return 0