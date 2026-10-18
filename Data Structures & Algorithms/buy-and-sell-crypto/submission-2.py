class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        for i in range(len(prices)):
            for j in range(i,len(prices)):
                t = prices[j] - prices[i]
                if t > mp:
                    mp = t
        return mp

    def maxProfitOn(self, prices: List[int]) -> int:
        max_profit = 0
        for i,x in enumerate(prices):
            if prices[i+1:] and x < max(prices[i+1:]):
                max_profit = max(max_profit, max(prices[i+1:]) - x )
        return max_profit

