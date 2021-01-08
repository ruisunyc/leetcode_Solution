class Solution:
    def countPrimes(self, n: int) -> int:
        if n<2:return 0
        dp = [1]*n
        dp[0] =dp[1] = 0
        for i in range(2,int(sqrt(n))+1):
            if dp[i]:
                dp[i*i:n:i] = [0]*len(dp[i*i:n:i] )
        return sum(dp)
