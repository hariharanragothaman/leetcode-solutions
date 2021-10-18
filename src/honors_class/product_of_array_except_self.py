from typing import List

def products_except_self(nums: List[int]) -> List[int]:
    output = []
    tmp = 1

    # here we are excluding the last number...
    for i in range(len(nums)):
        output.append(tmp)
        tmp = tmp * nums[i]

    tmp2 = 1
    # now do one more pass - for reverse traversal
    for i in range(len(nums)-1, -1, -1):
        output[i] = tmp2 * output[i]
        tmp2 = tmp2 * nums[i]

    print(*output)
    return output


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    # O/P - [24, 12, 8, 6]
    products_except_self(nums)