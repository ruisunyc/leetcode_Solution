class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:           
        m = len(heightMap)
        n = len(heightMap[0])
        if m<=2 or n<=2:return 0
        heap = []
        vis = set()    
        #访问第一行和最后一行
        for j in range(n):
            heapq.heappush(heap,(heightMap[0][j],0,j))
            heapq.heappush(heap,(heightMap[m-1][j],m-1,j))
            vis.add((0,j))
            vis.add((m-1,j))
        #访问第1列和最后一列
        for i in range(1,m-1):
            heapq.heappush(heap,(heightMap[i][0],i,0))
            heapq.heappush(heap,(heightMap[i][n-1],i,n-1))
            vis.add((i,0))
            vis.add((i,n-1))
        imax = float('-inf')
        ans = 0
        while heap:
            height,i,j = heapq.heappop(heap)
            imax = max(imax,height)
            for x,y in ((i+1,j),(i,j+1),(i-1,j),(i,j-1)):
                if 0<=x<m and 0<=y<n and (x,y) not in vis:
                    vis.add((x,y))
                    heapq.heappush(heap,(heightMap[x][y],x,y))
                    if imax>heightMap[x][y]:
                        ans+=imax-heightMap[x][y]
        return ans


