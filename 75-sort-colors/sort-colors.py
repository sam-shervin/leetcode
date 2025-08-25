class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l, mid, h = 0, 0, len(nums) - 1
        
        while mid <= h:
            if nums[mid] == 0:
                nums[l], nums[mid] = nums[mid], nums[l]
                l += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[h] = nums[h], nums[mid]
                h -= 1
