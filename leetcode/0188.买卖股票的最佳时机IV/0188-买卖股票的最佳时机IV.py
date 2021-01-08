class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n=len(prices)
        if not n:return 0
        # if k >= n//2:   # 退化为不限制交易次数
        #     profit = 0
        #     for i in range(1, n):
        #         if prices[i] > prices[i - 1]:
        #             profit += prices[i] - prices[i - 1]
        #     return profit
        # @lru_cache(None)
        # def dfs(index,status,i):
        #     if index==n or i==k:return 0            
        #     a = dfs(index+1,status,i) 
        #     b,c = 0,0           
        #     if status:#可卖出状态                
        #         b =dfs(index+1,0,i+1)+prices[index]
        #     else:#可买入状态
        #         c = dfs(index+1,1,i)-prices[index]
        #     return max(a,b,c)
        # return dfs(0,0,0)
        dp = [[0, -prices[0]] for _ in range(k+1)] 
        for i in range(1, n):
            for j in range(1, k+1):
                dp[j][0] = max(dp[j][0], dp[j][1] + prices[i])
                dp[j][1] = max(dp[j][1], dp[j - 1][0] - prices[i])        
        return dp[k][0]