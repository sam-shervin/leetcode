class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n= len(nums)
        xor1 = 0
        xor2=0
        for i in range(n):
            xor1^=nums[i]
            xor2^=i
        xor2^=n
        return xor1^xor2
        