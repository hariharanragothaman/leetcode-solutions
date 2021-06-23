def product_except_self(nums):
    output = []
    p = 1
    for i in range(len(nums)):
        output.append(p)
        p = p * nums[i]

    p = 1
    for i in range(len(nums) - 1, -1, -1):
        output[i] = output[i] * p
        p = p * nums[i]
    return output


nums = [1, 2, 3, 4]
result = product_except_self(nums)
print(result)
