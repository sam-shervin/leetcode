class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        longest = 0
        last_seen = {}
        for j, ch in enumerate(s):
            if ch in last_seen:
                i = max(i, last_seen[ch] + 1)
            last_seen[ch] = j
            longest = max(longest, j - i + 1)
        return longest
