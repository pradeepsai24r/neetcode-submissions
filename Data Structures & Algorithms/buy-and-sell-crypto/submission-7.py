class Solution:
    def maxProfitBF(self, prices: List[int]) -> int:
        mp = 0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                t = prices[j] - prices[i]
                if t > mp:
                    mp = t
        return mp

    def maxProfit1(self, prices: List[int]) -> int:
        max_profit = 0
        for i,x in enumerate(prices):
            if prices[i+1:] and x < max(prices[i+1:]):
                max_profit = max(max_profit, max(prices[i+1:]) - x )
        return max_profit

    # def maxProfit(self, prices: List[int]) -> int: 
    #     min_index = prices.index(min(prices))
    #     if min_index == len(prices)-1:
    #         prices.remove(min(prices))
    #         self.maxProfit(prices)
    #     mp = max(prices[min_index:]) - prices[min_index] 
    #     return mp

    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit