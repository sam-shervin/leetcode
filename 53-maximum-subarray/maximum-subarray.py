class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summ = 0
        maximum = float('-inf')
        for i in range(len(nums)):
            summ+=nums[i]
            if summ>maximum:
                maximum = summ
            if summ<0:
                summ = 0  
        return maximum      