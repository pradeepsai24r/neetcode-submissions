class Solution:
    """
    PS: [] --> CODE --> max_profit (int)
    inps:
    []
    [1,2]
    [3]
    [6,5,4]
    """

    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        for i, x in enumerate(prices):
            if prices[i+1:] and x < max(prices[i+1:]):
                mp = max(mp, max(prices[i+1:])-x)
        return mp

    def maxProfit1(self, prices: List[int]) -> int:
        res = 0
        if len(prices) < 2:
            return 0
        elif len(prices) == 2:
            d = prices[1] - prices[0]
            res = d if d > 0 else 0
            return res
        
        ### beyond edge cases
        first_min = min(prices)
        first_min_index = prices.index(first_min)
        if first_min_index == len(prices)-1:
            return 0
        next_max = max(prices[first_min_index+1:]) if prices[first_min_index+1:] else 0
        if next_max - first_min > 0:
            res = next_max - first_min
        return res



    def maxProfitBF(self, prices: List[int]) -> int: ## O(n^2)
        max_prt = 0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                prt = prices[j] - prices[i]
                max_prt = max(max_prt, prt)
        return max_prt
                