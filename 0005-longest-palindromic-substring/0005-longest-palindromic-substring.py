class Solution:
    def isPalindrome(self, s:str):
        for i in range(len(s)//2):
            if s[i] != s[len(s)-i-1]:
                return False
        return True
    def longestPalindrome(self, s: str) -> str:
        if (len(s) == 1):
            return s
        flag = ''
        for i in range(1, len(s)+1):
            for j in range(0, len(s)-i+1):
                string = s[j:j+i]
                if self.isPalindrome(string):
                    flag = string
                    break
        return flag