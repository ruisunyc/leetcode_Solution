class Solution:
    def superEggDrop(self, K: int, N: int) -> int:

        # @functools.lru_cache(None)
        # def dfs(k,n):
        #     if k==1:return n 
        #     if n==1:return 1
        #     return dfs(k,n-1)+dfs(k-1,n-1)+1
        # for i in range(1,N+1):
        #     if dfs(K,i)>=N:return i
        dp = [[0]*(N+1) for _ in range(K+1)]
        for i in range(1,K+1):
            for j in range(1,N+1):
                dp[i][j] = dp[i][j-1]+dp[i-1][j-1]+1
                if dp[K][j]>=N:
                    return j
