class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def rob_linear(start: int, end: int) -> int:
            prev1 = 0
            prev2 = 0
            for i in range(start, end):
                curr = max(prev2, prev1 + nums[i])
                prev1, prev2 = prev2, curr
            return prev2

        return max(rob_linear(0, len(nums)-1), rob_linear(1, len(nums)))