class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m,n = len(mat),len(mat[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]+mat[i-1][j-1]
        def get(x1,y1,x2,y2):
            x1 = min(m,max(x1,0))
            x2 = min(m,max(x2,0))
            y1 = min(n,max(y1,0))
            y2 = min(n,max(y2,0))
            return dp[x2][y2]+dp[x1][y1]-dp[x1][y2]-dp[x2][y1]
        for i in range(m):
            for j in range(n):
                mat[i][j] = get(i-K,j-K,i+K+1,j+K+1)
        return mat