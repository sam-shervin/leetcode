class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums)-1
        while(l<=h):
            m = (l+h)//2
            if nums[m]==target:
                return m
            if nums[m]<=nums[h]:
                if nums[m]<target<=nums[h]:
                    l = m+1
                else:
                    h = m-1
            else:
                if nums[l]<=target<nums[m]:
                    h=m-1
                else:
                    l=m+1
        return -1
        