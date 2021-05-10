"""
Given a unsorted integer array - find the smallest missing positive integer
I/P: [1, 2, 0]
O/P: 3

I/P: [3, 4, -1, 1]
O/P: 2

I/P: [7, 8, 9, 11, 12]
O/P: 1
"""

def first_missing_positive(nums):
    # First step, let's remove all the negative numbers
    nums = [c for c in nums if c > 0]
    nums.sort()
    missing = 1

    for i in range(len(nums)):
        if nums[i] == missing:
            missing += 1
    return missing

"""
The core idea is like - building the list from  1...n 
So, only if the value is present we increment it 
"""