class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        mid = 0
        n = len(nums)-1
        while mid<=n:
            if nums[mid] == 0:
                nums[mid], nums[i] = nums[i], nums[mid]
                i+=1; mid+=1;
            elif nums[mid] == 1:
                mid+=1;
            else:
                nums[mid], nums[n] = nums[n], nums[mid]
                n-=1;

        