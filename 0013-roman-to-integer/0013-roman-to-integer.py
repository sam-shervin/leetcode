class Solution:
    def romanToInt(self, s: str) -> int:
        a = ('I', 'V', 'X', 'L', 'C', 'D', 'M')
        b = ('1', '5', '10', '50', '100', '500', '1000')
        c = ''
        prev = 7
        boo = False
        for i in range(len(s)):
            if a.index(s[i]) > prev:
                if i>0:
                    if c.count('+') == 1:
                        c = '-' + c
                    else:
                        c = ((c[::-1][1:]).replace('+', '-', 1))[::-1] + '+'
                    
                    
            c+=(b[a.index(s[i])] + '+')
            
            if i == len(s)-1:
                c = c[:len(c)-1]
            prev = a.index(s[i])
        return eval(c)