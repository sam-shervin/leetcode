class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [0] * (amount+1)
        for i in range(1, amount+1):
            minn = float('inf')
            for c in coins:
                diff = i - c
                if diff < 0:
                    break
                minn = min(minn, 1 + dp[diff])
            dp[i] = minn
        minn = dp[amount]
        return -1 if minn == float('inf') else minn
