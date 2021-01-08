class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = buy2 = float('inf')
        profit1 = profit2 = 0
        for num in prices:
            buy1 = min(buy1,num) #比较第一次买入的最小价格
            profit1 = max(profit1,num-buy1) #获取第一次交易的最大利润
            buy2 = min(buy2,num-profit1) #获取第二次买入的最小价格，相当于减去第一次的利润
            profit2 = max(profit2,num-buy2)#获取第二次交易的最大利润
        return profit2