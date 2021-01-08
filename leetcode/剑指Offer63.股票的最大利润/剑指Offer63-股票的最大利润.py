class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mins = float('inf')
        res = 0
        for num in prices:
            mins  = min(mins,num)
            res  = max(res,num-mins)
        return res