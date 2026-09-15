class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1

        profit = 0
        min_val = float('Inf') 

        for price in prices:
            min_val = min(min_val, price)
            profit = max(profit, price - min_val)
        return profit