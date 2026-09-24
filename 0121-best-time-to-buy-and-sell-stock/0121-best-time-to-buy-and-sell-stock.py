class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            # Update minimum purchase price seen so far
            if price < min_price:
                min_price = price
            # Calculate potential profit if sold today and update max profit
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit