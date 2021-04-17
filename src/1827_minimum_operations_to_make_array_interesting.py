from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        cnt = 0
        for i in range(1, len(nums)):
            diff = 0
            if nums[i] <= nums[i-1]:
                diff = nums[i-1] - nums[i]
                cnt += diff + 1
                nums[i] = nums[i] + diff + 1
                print(*nums)
                print("The diff is:", diff)
            else:
                continue

        print(cnt)
        return cnt


if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 1]
    s.minOperations(nums)