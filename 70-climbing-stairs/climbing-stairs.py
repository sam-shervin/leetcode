class Solution:
    memo = {}
    def dp(self, n):
        if n==0 or n==1:
            return 1
        if n in self.memo:
            return self.memo[n]
        self.memo[n] = self.dp(n-1)+self.dp(n-2)
        return self.memo[n]
    def climbStairs(self, n: int) -> int:
        return self.dp(n)
        