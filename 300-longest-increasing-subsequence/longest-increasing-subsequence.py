class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for num in nums:
            left, right = 0, len(sub) - 1
            idx = len(sub)
            while left <= right:
                mid = (left + right) // 2
                if sub[mid] >= num:
                    idx = mid
                    right = mid - 1
                else:
                    left = mid + 1
            if idx == len(sub):
                sub.append(num)
            else:
                sub[idx] = num
        return len(sub)
