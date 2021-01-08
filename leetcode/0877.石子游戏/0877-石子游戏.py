class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # dp = [[0]*len(piles) for _ in range(len(piles))]
        # for i in range(len(piles)-2,-1,-1):
        #     for j in range(i,len((piles))):
        #         dp[i][j] = max(piles[i]-dp[i+1][j],piles[j]-dp[i][j-1])
        # return dp[0][len(piles)-1]>0

        dp = [0]*len(piles)
        for i in range(len(piles)-2,-1,-1):
            for j in range(i,len((piles))):
                dp[j] = max(piles[i]-dp[j],piles[j]-dp[max(0,j-1)])
        return dp[len(piles)-1]>0
        
        
