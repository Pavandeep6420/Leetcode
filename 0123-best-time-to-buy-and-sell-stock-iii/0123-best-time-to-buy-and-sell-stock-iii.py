class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        first_buy, first_sell = float('inf'), 0
        second_buy, second_sell = float('inf'), 0
        
        for price in prices:
            # First transaction: minimum cost and maximum profit
            first_buy = min(first_buy, price)
            first_sell = max(first_sell, price - first_buy)
            
            # Second transaction: minimum effective cost considering profit from first sale
            second_buy = min(second_buy, price - first_sell)
            second_sell = max(second_sell, price - second_buy)
            
        return second_sell