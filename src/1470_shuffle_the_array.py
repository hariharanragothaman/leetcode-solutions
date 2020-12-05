"""
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
Return the array in the form [x1,y1,x2,y2,...,xn,yn].
"""

def shuffle(nums):
    split = len(nums) // 2
    first_p, second_p = nums[:split], nums[split:]
    output = []
    for c in zip(first_p, second_p):
        output.append(c[0])
        output.append(c[1])
    return output


if __name__ == '__main__':
    nums = [2,5,1,3,4,7]
    res = shuffle(nums)
    print(res)