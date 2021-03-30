from functools import reduce
import operator
import math

class Solution:
    def numTrees(self, n: int) -> int:
        nCr = lambda n, r: reduce(operator.mul, range(n - r + 1, n + 1), 1) // math.factorial(r)
        catalan = lambda n: nCr(2 * n, n) // (n + 1)
        return catalan(n)