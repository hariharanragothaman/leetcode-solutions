"""
Given an array nums, return true if the array was originally sorted in non-decreasing order,
then rotated some number of positions (including zero). Otherwise, return false.

There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length],
where % is the modulo operation.



Example 1:

Input: nums = [3,4,5,1,2]
Output: true
Explanation: [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 3 positions to begin on the the element of value 3: [3,4,5,1,2].
Example 2:

Input: nums = [2,1,3,4]
Output: false
Explanation: There is no sorted array once rotated that can make nums.
Example 3:

Input: nums = [1,2,3]
Output: true
Explanation: [1,2,3] is the original sorted array.
You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.
Example 4:

Input: nums = [1,1,1]
Output: true
Explanation: [1,1,1] is the original sorted array.
You can rotate any number of positions to make nums.
Example 5:

Input: nums = [2,1]
Output: true
Explanation: [1,2] is the original sorted array.
You can rotate the array by x = 5 positions to begin on the element of value 2: [2,1].
"""

# The key concept is - how many times can you rotate something to get itself back? Hmm..
# Key-Logic: Okay so when we compare neighbours of A - a > b can happen at most only once.
# The first and last element are connected

# --> This string logic won't work here, since - we have numbers like 10 and duplicates also. Haha
def check_initial_thoughts(nums):
    nums = ''.join(str(c) for c in nums)
    total = ''.join(str(c) for c in sorted(nums))
    temp = total*2
    if nums in temp:
        return True
    return False

def check(nums):
    print("Some debugging here")
    print(nums[1:]+nums[:1])
    # This is to cyclically compare the neigbhours.
    cnt = 0
    for a, b in zip(nums, nums[1:] + nums[:1]):
        if a > b:
            cnt += 1
    if cnt <= 1:
        return True
    return False


if __name__ == '__main__':
    nums = [2, 1, 3, 4]
    result = check(nums)
    print(result)