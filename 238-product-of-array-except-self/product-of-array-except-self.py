import numpy as np
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        # Compute prefix in-place
        for i in range(1, n):
            answer[i] = answer[i - 1] * nums[i - 1]

        # Compute suffix and final result in one pass
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer
