class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not any(matrix):return 0
        m = len(matrix)
        n=len(matrix[0])
        mem = [[0]*n for _ in range(m)]
        def dfs(i,j):
            if mem[i][j]!=0:return mem[i][j]
            ans = 1
            for x,y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                if 0<=x<m and 0<=y<n and matrix[x][y]>matrix[i][j]:
                    ans = max(ans,dfs(x,y)+1)
            mem[i][j] = ans
            return ans
        return max(dfs(i,j) for i in range(m) for j in range(n))
