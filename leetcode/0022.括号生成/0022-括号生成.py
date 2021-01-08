class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def dfs(s,left,right):
            if left==n and right==n:
                ans.append(s)
                return
            if left<n:
                dfs(s+'(',left+1,right)
            if left>right:
                dfs(s+')',left,right+1)
        dfs('',0,0)
        return ans
