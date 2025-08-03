class Solution:
    def countSubstrings(self, s: str) -> int:
        l = len(s)
        count = 0
        for i in range(l):
            left, right = i, i
            while left>-1 and right<len(s):
                if s[left]==s[right]:
                    count+=1
                    left-=1
                    right+=1
                else:
                    break
            left, right = i, i+1
            while left>-1 and right<len(s):
                if s[left]==s[right]:
                    count+=1
                    left-=1
                    right+=1
                else:
                    break
        return(count)