class Solution:
    def permutation(self, s: str) -> List[str]:
        s=''.join(sorted(s))
        ans = []
        def dfs(s,tmp):
            if not s:
                ans.append(tmp)
            for i in range(len(s)):
                if i>0 and s[i-1]==s[i]:continue
                dfs(s[:i]+s[i+1:],tmp+s[i])
        dfs(s,'')
        return ans
            
