from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []  # stores the smallest possible tail of increasing subsequences

        for num in nums:
            # Find index in sub where num can replace or be appended
            idx = bisect_left(sub, num)

            if idx == len(sub):
                # num is bigger than any element in sub -> append
                sub.append(num)
            else:
                # Replace the element at idx with num (better candidate)
                sub[idx] = num

        return len(sub)
