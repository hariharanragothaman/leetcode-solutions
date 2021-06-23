"""
Basically  each kid has x number of x number of candies
Then, there are a few extra candies, we are basically trying to see, 
if a kids gets the extra candies, will it be greater than equal to maximum
"""


def kidswithCandies(candies, extra):
    max_value = max(candies)
    result = [False] * len(candies)
    for i, c in enumerate(candies):
        if c + extra >= max_value:
            result[i] = True
    return result


if __name__ == "__main__":
    op = kidswithCandies([2, 3, 5, 1, 3], 3)
    print(op)
