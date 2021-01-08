class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        ans = []
        def dfs(row,tmp,cols,sums,subs):
            if row==n:
                ans.append(tmp)
                return
            for j in range(n):
                if j not in cols and row+j not in sums and row-j not in subs:
                    dfs(row+1,tmp+[j],cols|{j},sums|{row+j},subs|{row-j})
        dfs(0,[],set(),set(),set())
        return [['.'*i+'Q'+'.'*(n-i-1) for i in cur] for cur in ans]