class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            a = prices[i]-m
            if profit<a:
                profit = a
            if m>prices[i]:
                m = prices[i]
        return profit        