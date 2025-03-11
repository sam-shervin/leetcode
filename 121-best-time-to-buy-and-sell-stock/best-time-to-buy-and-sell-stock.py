class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            c = prices[i] - m
            if prices[i] < m:
                m = prices[i]
            if profit < c:
                profit = c
        return profit

        