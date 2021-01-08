class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [1]        
        for i in range(1,rowIndex+1):
            dp=[1]+[dp[j]+dp[j+1] for j in range(i-1)]+[1]
        return dp