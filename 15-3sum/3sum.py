class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 2):
            a = nums[i]
            if a > 0:
                break
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, n - 1
            while l < r:
                b, c = nums[l], nums[r]
                total = a + b + c
                if total == 0:
                    res.append([a, b, c])
                    while l < r and nums[l] == b:
                        l += 1
                    while l < r and nums[r] == c:
                        r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1

        return res
