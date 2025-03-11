class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            cost = prices[i] - mini
            if prices[i] < mini:
                mini = prices[i]
            if profit < cost:
                profit = cost
        return profit

        