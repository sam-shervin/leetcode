class Solution:
    def __init__(self):
        self.memo = {0: 0}
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        if amount in self.memo:
            return self.memo[amount]

        minn = float('inf')
        for c in coins:
            diff = amount - c
            if diff < 0:
                break
            res = self.coinChange(coins, diff)
            if res == -1:
                continue
            minn = min(minn, 1 + res)

        self.memo[amount] = minn
        return -1 if minn == float('inf') else minn
