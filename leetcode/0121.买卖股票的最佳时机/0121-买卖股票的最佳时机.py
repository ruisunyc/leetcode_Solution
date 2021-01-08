class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mins = float('inf')
        profit = 0
        for num in prices:
            mins= min(mins,num)   
            profit = max(profit,num-mins)                   
        return profit