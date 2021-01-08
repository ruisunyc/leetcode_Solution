class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n= len(grid[0])
        k = min(k,m+n-3)
        if k<0:return 0
        vis = set()
        q = deque([(0,0,k,0)])
        while q:
            i,j,res,step = q.popleft()            
            for x,y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                if 0<=x<m and 0<=y<n:
                    if x==m-1 and y==n-1:return step+1
                    curres = res-grid[x][y]
                    if curres<0:continue
                    if (x,y,curres) not in vis:
                        vis.add((x,y,curres) )
                        q.append((x,y,curres,step+1))
        return -1

                    
