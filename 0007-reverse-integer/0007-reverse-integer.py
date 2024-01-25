class Solution:
    def reverse(self, x):
        y=x
        x=abs(x)  
        out=0
        while(x!=0):
            out*=10
            out+=(x%10)
            x=x//10
        return (out if y>=0 else -out) if (-2**31 <= out <= 2**31 - 1) else 0

