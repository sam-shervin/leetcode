class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        n = len(s)
        longest = 0
        last_seen = {}
        while j<n:
            if s[j] in last_seen:
                i = max(i, last_seen[s[j]] + 1)
            last_seen[s[j]] = j
            longest = max(longest, len(s[i:j+1]))
            j+=1
        return longest
