class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        row = [set(map(str,[i for i in range(1,10)])) for _ in range(9)]
        col = [set(map(str,[i for i in range(1,10)])) for _ in range(9)]
        block = [set(map(str,[i for i in range(1,10)])) for _ in range(9)]
        ans = []
        for i in range(9):
            for j in range(9):
                cur = board[i][j]
                if cur!='.':
                    row[i].remove(cur)
                    col[j].remove(cur)
                    block[i//3*3+j//3].remove(cur)
                else:
                    ans.append([i,j])        
        def dfs(i):
            if i==len(ans):return True
            x,y = ans[i]
            for one in row[x] & col[y] & block[x//3*3+y//3]:
                board[x][y] = one
                row[x].remove(one)
                col[y].remove(one)
                block[x//3*3+y//3].remove(one)
                if dfs(i+1):return True
                row[x].add(one)
                col[y].add(one)
                block[x//3*3+y//3].add(one)
        dfs(0)