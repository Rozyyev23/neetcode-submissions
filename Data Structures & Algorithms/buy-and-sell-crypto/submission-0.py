class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        k = 0
        max_profit = 0

        while k < len(prices):
            min_price = min(min_price, prices[k])
            max_profit = max(max_profit, prices[k] - min_price)
            k += 1
        return max_profit