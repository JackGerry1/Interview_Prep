from typing import List

def maxProfit(prices: List[int]) -> int:
    l = 0 
    r = 1
    max_profit = 0 
    
    while r < len(prices): 
        if prices[l] < prices[r]: 
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)
        
        else: 
            l = r
        r += 1
    
    return max_profit
    

def maxProfitV2(prices: List[int]) -> int:
    max_profit = 0 
    min_buy = prices[0]
    
    for price in prices: 
        profit = price - min_buy
        
        max_profit = max(max_profit, profit)
        
        min_buy = min(min_buy, price)
    
    return max_profit

prices1 = [10,1,5,6,7,1, 23]
prices2 = [10,8,7,5,2, 23]

print(maxProfit(prices2))
print(maxProfitV2(prices2))