# class Solution:
#     def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
#         m, n = len(mat), len(mat[0])
#         P = [[0] * (n + 1) for _ in range(m + 1)]
#         for i in range(1, m + 1):
#             for j in range(1, n + 1):
#                 P[i][j] = P[i - 1][j] + P[i][j - 1] - P[i - 1][j - 1] + mat[i - 1][j - 1]
        
#         def getRect(x1, y1, x2, y2):
#             return P[x2][y2] - P[x1 - 1][y2] - P[x2][y1 - 1] + P[x1 - 1][y1 - 1]
        
#         r, ans = min(m, n), 0
#         for i in range(1, m + 1):
#             for j in range(1, n + 1):
#                 for c in range(ans + 1, r + 1):
#                     if i + c - 1 <= m and j + c - 1 <= n and getRect(i, j, i + c - 1, j + c - 1) <= threshold:
#                         ans += 1
#                     else:
#                         break
#         return ans

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
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
        ans = 0
        for i in range(m):
            for j in range(n):
                for c in range(ans+1,min(m,n)+1):
                    if i+c<=m and j+c<=n and get(i,j,i+c,j+c)<=threshold:
                        ans +=1
                    else:
                        break
        return ans