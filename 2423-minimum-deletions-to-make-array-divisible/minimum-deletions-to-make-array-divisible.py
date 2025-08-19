from math import gcd
from functools import reduce

class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        g = reduce(gcd, numsDivide)
        nums.sort()
        for i, x in enumerate(nums):
            if g % x == 0:
                return i
            elif x > g:
                break
                
        return -1
