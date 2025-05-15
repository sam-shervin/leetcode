import numpy as np
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums = np.array(nums)
        prefix = np.cumprod(np.insert(nums[:-1], 0, 1))
        suffix = np.cumprod(np.insert(nums[::-1][:-1], 0, 1))[::-1]
        return (prefix * suffix).tolist()
