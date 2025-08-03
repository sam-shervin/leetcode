from bisect import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for num in nums:
            idx = bisect(sub, num)
            if idx == 0 or (idx > 0 and sub[idx - 1] < num):
                if idx == len(sub):
                    sub.append(num)
                else:
                    sub[idx] = num
        return len(sub)
