class Solution:
    def pathWithObstacles(self, obstacleGrid: List[List[int]]) -> List[List[int]]:
        self.ans = []
        if not any(obstacleGrid):
            return self.ans
        r = len(obstacleGrid)
        c = len(obstacleGrid[0])
        def dfs(tmp):
            i,j = tmp[-1]
            if obstacleGrid[i][j]!=1:
                obstacleGrid[i][j]=1
                if i==r-1 and j==c-1:
                    self.ans = tmp
                    return True  
                for x,y in ((i+1,j),(i,j+1)):
                    if 0<=x<r and 0<=y<c and obstacleGrid[x][y]!=1:
                        if dfs(tmp+[[x,y]]):return True
        dfs([[0,0]])
        return self.ans