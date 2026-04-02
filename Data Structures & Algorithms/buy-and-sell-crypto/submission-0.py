class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        profit = 0
        buyPoint = prices[0]
        sellPoint = 0
        for i in range(1, len(prices)):
            sellPoint = prices[i]
            if buyPoint>sellPoint:
                buyPoint = sellPoint
            else:
                profit = max(profit, (sellPoint-buyPoint))

        return profit
        