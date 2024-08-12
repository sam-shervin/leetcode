class Solution:
    def check(self, s:str, l:int, r:int, max_length:int, pres_s):
        string = pres_s
        while l>=0 and r<len(s) and s[l] == s[r]:
            palindrome = s[l:r+1]
            if len(palindrome) > max_length:
                max_length = len(palindrome)
                string = palindrome
            l-=1
            r+=1
        return string, max_length
        
    def longestPalindrome(self, s: str) -> str:
        if (len(s) == 1):
            return s
        max_length = 0
        long_palindrome = s
        for i in range(len(s)):
            long_palindrome, max_length = self.check(s, i,i, max_length, long_palindrome)
            long_palindrome, max_length = self.check(s, i, i+1, max_length, long_palindrome)
            
        return long_palindrome