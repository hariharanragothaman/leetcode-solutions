"""
Given scores of N athletes, find their relative ranks and the people with the top three highest scores,
who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal".
For the left two athletes, you just need to output their relative ranks according to their scores.

Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal".
For the left two athletes, you just need to output their relative ranks according to their scores.

"""


class Solution:
    def findRelativeRanks(self, nums):
        nu, hmap = sorted(nums, reverse=True), {}
        for i, c in enumerate(nu, 1):
            hmap[c] = i

        rank_map = {1: 'Gold Medal', 2: "Silver Medal", 3: "Bronze Medal"}

        for k, v in hmap.items():
            if v in rank_map:
                hmap[k] = rank_map[v]

        for i, c in enumerate(nums):
            nums[i] = str(hmap[c])

        return nums
