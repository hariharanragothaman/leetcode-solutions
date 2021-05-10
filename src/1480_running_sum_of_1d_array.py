import operator
from itertools import accumulate

def running_sum(nums):
    n = list(accumulate(nums, operator.add))
    return n

if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    op = running_sum(nums)
    print(op)