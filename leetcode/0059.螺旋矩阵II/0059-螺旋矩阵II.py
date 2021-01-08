class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        left,right,top,bot = 0,n-1,0,n-1
        mat = [[0]*n for _ in range(n)]
        num,end = 1,n*n
        while num<=end:
            for j in range(left,right+1):
                mat[top][j]=num 
                num+=1
            top+=1
            for j in range(top,bot+1):
                mat[j][right]=num 
                num+=1
            right-=1
            for j in range(right,left-1,-1):
                mat[bot][j] = num
                num+=1
            bot-=1
            for j in range(bot,top-1,-1):
                mat[j][left]=num 
                num+=1
            left+=1
        return mat