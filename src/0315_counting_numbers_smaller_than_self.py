"""
Counting numbers smaller than self.

Problem Statement:

You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].



Example 1:

Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.

Example 2:

Input: nums = [-1]
Output: [0]

Example 3:

Input: nums = [-1,-1]
Output: [0,0]



Constraints:

    1 <= nums.length <= 105
    -104 <= nums[i] <= 104


"""


# Approach number 1 - using binary search

from typing import List
import bisect


def count_smaller(nums: List[int]) -> List[int]:
    sorted_arr, count_arr = [], []
    for num in nums[::-1]:
        index = bisect.bisect_left(sorted_arr, num)
        count_arr.append(index)
        sorted_arr.insert(index, num)
    return count_arr[::-1]


if __name__ == "__main__":
    nums = [5, 2, 6, 1]
    count = count_smaller(nums)
    print(count)
