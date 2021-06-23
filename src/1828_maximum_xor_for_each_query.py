from typing import List
from functools import reduce


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        result = []

        limit = 2 ** maximumBit
        max_limit = "1" * (limit.bit_length())
        print("max_limit is:", max_limit)
        number_of_bits = len(max_limit) - 1

        prefix_xor = [nums[0]]
        for i in range(1, len(nums)):
            tmp = nums[i] ^ prefix_xor[-1]
            prefix_xor.append(tmp)

        print("The prefix_xor is:", prefix_xor)

        for i in range(len(nums)):
            val = ((1 << number_of_bits) - 1) ^ prefix_xor[-1]
            prefix_xor.pop()
            result.append(val)
        print(*result)
        return result


if __name__ == "__main__":
    s = Solution()
    print(2 ** 20)
    nums = [0, 1, 2, 2, 5, 7]
    print(reduce(lambda i, j: i ^ j, nums))
    maximumBit = 3
    s.getMaximumXor(nums, maximumBit)
