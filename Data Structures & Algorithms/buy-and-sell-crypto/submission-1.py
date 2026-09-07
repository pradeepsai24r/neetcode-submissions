class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i,x in enumerate(prices):
            if prices[i+1:] and x < max(prices[i+1:]):
                max_profit = max(max_profit, max(prices[i+1:]) - x )
        return max_profit

