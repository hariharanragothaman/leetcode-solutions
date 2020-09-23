"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""
# Method1 - This is just the brute-force way of doing stuff.
def two_sums1(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# Method2
# Time complexity is O(n) and space complexity is O(n)
def two_sum(nums, target):
    h_map = {}
    for i, n in enumerate(nums):
        h_map[n] = i

    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in h_map and h_map[diff] !=i:
            return [i, h_map[diff]]