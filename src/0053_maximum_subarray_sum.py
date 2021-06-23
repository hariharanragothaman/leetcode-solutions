"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""
# there are several approaches - Greedy, DP, Sliding Window etc.
# Let's analyze each of those methods.

# SOLUTION1: Sliding Window


def maximum_sub_array(nums):
    left, right = 0, 0
    max_sum = nums[left]
    window_sum = 0

    for i in range(len(nums)):
        window_sum += nums[right]
        max_sum = max(window_sum, max_sum)
        right += 1

        while left < right and window_sum < 0:
            window_sum -= nums[left]
            left -= 1
    return max_sum
