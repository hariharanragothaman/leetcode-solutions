"""
Given an array A of length n - whose entries are integers, compute the largest product except one.
Array entries can be -ve,+ve, 0
Cannot use division
"""
import operator
import typing

"""
So one approach - is to get the overall product and divide each number by that product ~ O(n^2)
"""

from typing import *
from itertools import accumulate


arr = [3, 2, 5, 4]

def find_biggest_n_minus_one_product(A: List[int]) -> int:
    suffix_products = list(accumulate(reversed(A), operator.mul))
    print(suffix_products)
    suffix_products = suffix_products[::-1]

    prefix_product = 1
    max_product = float('-inf')

    for i in range(len(A)):
        suffix_product = suffix_products[i+1] if i+1 < len(A) else 1
        max_product = max(max_product, prefix_product * suffix_product)
        prefix_product = prefix_product * A[i]

    return typing.cast(int, max_product)

ans = find_biggest_n_minus_one_product(arr)
print(ans)