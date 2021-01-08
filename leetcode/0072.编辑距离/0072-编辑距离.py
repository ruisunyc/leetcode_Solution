class Solution:   
    def minDistance(self, word1: str, word2: str) -> int:
        @functools.lru_cache(None)
        def dfs(word1,word2):            
            if not word1 or not word2:
                return len(word1)+len(word2)            
            if word1[0]==word2[0]:
                return dfs(word1[1:],word2[1:]) 
            return min(dfs(word1,word2[1:]),dfs(word1[1:],word2),dfs(word1[1:],word2[1:]))+1
        return dfs(word1,word2)
        # n1,n2 = len(word1)+1,len(word2)+1
        # dp = [[0]*(n2) for _ in range(n1)]        
        # for i in range(n1):
        #     for j in range(n2):
        #         if i==0:
        #             dp[i][j] = j
        #         elif j==0:
        #             dp[i][j] = i 
        #         else:
        #             if word1[i-1]==word2[j-1]:
        #                 dp[i][j] = dp[i-1][j-1]
        #             else:
        #                 dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1                
        # return dp[-1][-1]
        # vis = set()
        # q = deque([(word1,word2,0)])
        # while q:
        #     w1,w2,dis = q.popleft()
        #     if (w1,w2) not in vis:
        #         vis.add((w1,w2))
        #         if w1==w2:return dis
        #         while w1 and w2 and w1[0]==w2[0]:
        #             w1 = w1[1:]
        #             w2 = w2[1:]
        #         q.extend([(w1,w2[1:],dis+1),(w1[1:],w2,dis+1),(w1[1:],w2[1:],dis+1)])
