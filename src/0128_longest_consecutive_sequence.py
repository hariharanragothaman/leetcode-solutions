def longest_consecutive_sequence(nums):
    if not nums:
        return 0
    max_length, window_length = 0, 0
    nums = sorted(set(nums))

    for i in range(1, len(nums)):
        if (nums[i] - nums[i - 1]) == 1:
            window_length += 1
            max_length = max(window_length, max_length)
        else:
            window_length = 0
    return max_length + 1
