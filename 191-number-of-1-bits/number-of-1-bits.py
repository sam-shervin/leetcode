class Solution:
    def hammingWeight(self, n: int) -> int:
        MASK = 0x00000001
        cnt=0
        while n!=0:
            if MASK&n:
                cnt+=1
            n>>=1
        return cnt
        