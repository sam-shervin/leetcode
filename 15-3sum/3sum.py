class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            l, r = i+1, n-1
            while l<r:
                total = nums[i]+nums[l]+nums[r]
                if not total:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1

                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1
                elif total<0:
                    l+=1
                else:
                    r-=1
        return res

        