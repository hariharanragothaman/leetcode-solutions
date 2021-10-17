# Find the smallest positive integer that is not present in the array

from typing import *

arr = [3, 5, 4, -1, 5, 1, -1]

def find_first_missing_positive(A: List[int]) -> int:
    n = len(A)
    for i in range(n):
        while 1 <= A[i] <= len(A) and A[i] != A[A[i] -1]:
            A[A[i]-1], A[i] = A[i], A[A[i]-1]

    print("The array now after swapping is:", A)
    # now in the second pas, search through a for the first index of i
    # such that A[i] != i + 1
    # If all numbers are present then the next number is - len(A) + 1
    # next() takes default parameter
    return next((i+1 for i, a in enumerate(A) if a != i+1), len(A)+1)

output = find_first_missing_positive(arr)
print("The output is:", output)