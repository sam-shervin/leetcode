class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int):
            while left > -1 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        long_string = ""
        for i in range(len(s)):
            a = expand(i, i)
            b = expand(i, i + 1)
            if len(a)>len(long_string):
                long_string = a
            if len(b)>len(long_string):
                long_string = b
        return long_string