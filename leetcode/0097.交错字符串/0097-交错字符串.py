class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1,n2,n3=len(s1),len(s2),len(s3)
        if n1+n2!=n3:return False
        # @lru_cache(None)
        # def dfs(i,j,k):
        #     if i==il and j==jl and k==kl:return True
        #     if k>kl:return False
        #     if i<il and s1[i]==s3[k] and dfs(i+1,j,k+1):return True
        #     if j<jl and s2[j]==s3[k] and dfs(i,j+1,k+1):return True
        #     return False
        # return dfs(0,0,0)
        # dp = [[False]*(jl+1) for _ in range(il+1)] #s1的前i个字符与s2的前j个字符能否构成s3的前i+j个字符
        # dp[0][0]=True
        # for i in range(il+1):
        #     for j in range(jl+1):
        #         if i==0 and j==0:continue
        #         if i==0:
        #             dp[i][j] = dp[i][j-1] and s2[j-1] == s3[j-1]
        #         elif j==0:
        #             dp[i][j] = dp[i-1][j] and s1[i-1] == s3[i-1]
        #         else:
        #             dp[i][j] = (dp[i][j-1] and s2[j-1] == s3[i+j-1]) or (dp[i-1][j] and s1[i-1] == s3[i+j-1])
        # return dp[-1][-1]       
        q = collections.deque([(0,0,0)])
        visited = set()
        while q:
            i,j,k = q.popleft()
            if k==n3:return True
            if i<n1 and s1[i]==s3[k] and (i+1,j,k+1) not in visited:
                q.append((i+1,j,k+1))
                visited.add((i+1,j,k+1))
            if j<n2 and s2[j]==s3[k] and (i,j+1,k+1) not in visited:
                q.append((i,j+1,k+1))
                visited.add((i,j+1,k+1))
        return False