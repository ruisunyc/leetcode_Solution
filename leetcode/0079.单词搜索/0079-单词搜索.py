class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n,lens = len(board),len(board[0]),len(word)
        def dfs(i,j,boards,ind):
            if ind==lens-1:return True
            t = boards[i][j]
            boards[i][j] = '#'            
            for x,y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                if 0<=x<m and 0<=y<n and boards[x][y]==word[ind+1] and dfs(x,y,boards,ind+1):return True                    
            boards[i][j] = t       
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0] and dfs(i,j,board,0):
                    return True
        return False
