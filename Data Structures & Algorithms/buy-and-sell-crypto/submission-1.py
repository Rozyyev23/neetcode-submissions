class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        k, profit = 0, 0 

        while k < len(prices):
            min_price = min(min_price, prices[k])
            profit = max(profit, prices[k] - min_price)
            k += 1 
        return profit
    