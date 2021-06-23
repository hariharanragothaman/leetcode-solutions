"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
"""

"""
Solution Approaches Techniques:

1. Binary Search + DP - O(nlogn)
2. DP - O(n^2)

a. In binary search, we basically just use - bisect_left to construct the sorted array
b. We also smartly only append - when the index to be inserted is the len(array-being-built)
   else - we replace the number in that index.

OTOH - The classical DP approach is slightly varied
We can calculate the length of the increasing subsequence upto the ith index - finally we can return the max of it.

"""
import bisect


class Solution:
    def length_of_LIS_binary_search(self, nums) -> int:
        temp = []
        for number in nums:
            index = bisect.bisect_left(temp, number)

            if index == len(temp):
                temp.append(number)
            else:
                temp[index] = number

        return len(temp)

    def length_of_LIS_dp(self, nums) -> int:
        temp = [1] * len(nums)
        for i in range(1, len(arr)):
            for j in range(i):
                if arr[i] >= arr[j] and temp[i] <= temp[j] + 1:
                    temp[i] = temp[j] + 1

        max_length = 0
        for k in range(len(arr)):
            max_length = max(max_length, temp[k])
        return max_length


if __name__ == "__main__":
    sol = Solution()
    arr = [10, 9, 2, 5, 3, 7, 101, 18]
    op = sol.length_of_LIS(arr)
    print("The length of the longest increasing subsequence is:", op)
