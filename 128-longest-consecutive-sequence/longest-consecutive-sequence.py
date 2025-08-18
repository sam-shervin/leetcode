class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num-1 not in num_set:
                length = 1
                current = num
                while current+1 in num_set:
                    length+=1
                    current+=1
                longest = max(length, longest)
        return longest
