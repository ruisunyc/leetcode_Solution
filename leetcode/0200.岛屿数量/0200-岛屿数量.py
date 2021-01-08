class DSU:
    def __init__(self):
        self.f = {}
    def find(self,x):
        self.f.setdefault(x,x)
        if self.f[x]!=x:
            self.f[x] = self.find(self.f[x])
        return self.f[x]
    def unio(self,x,y):
        fx = self.find(x)
        fy = self.find(y)
        if fx!=fy:
            self.f[fx] = fy
class Solution:
    #²¢²é¼¯
    def numIslands(self, grid: List[List[str]]) -> int:
        dsu = DSU()
        m,n=len(grid),len(grid[0])        
        for i in range(m):
            for j in range(n): 
                if grid[i][j]=='1':                  
                    for dx,dy in ((1,0),(0,1)):
                        x,y=i+dx,j+dy
                        if 0<=x<m and 0<=y<n and grid[x][y]=='1':
                            dsu.unio(x*n+y,i*n+j)
        res = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':                   
                    res.add(dsu.find(i*n+j))
        return len(res)