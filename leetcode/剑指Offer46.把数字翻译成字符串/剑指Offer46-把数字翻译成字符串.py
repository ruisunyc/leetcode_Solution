class Solution:
    def translateNum(self, num: int) -> int:
        @functools.lru_cache(None)       
        def dfs(s):
            if not s:return 1
            ans = 0
            ans+=dfs(s[1:]) 
            if 10<=int(s[:2])<=25:
                ans+=dfs(s[2:])
            return ans
        return dfs(str(num))

        
