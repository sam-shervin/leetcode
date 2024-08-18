class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n<2:
            return 0
        jump = 0
        end = 0
        far = 0
        for i in range(n-1):
            far = max(i+nums[i], far)
            if i == end:
                jump+=1
                end = far
                if end == n-1:
                    break
        return jump
            
        