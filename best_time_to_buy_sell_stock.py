"""
leetcode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""

def maxProfit(prices):

    min_price = prices[0]
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        
        max_profit = max(max_profit, price - min_price) # current price - buying prince
    
    return max_profit