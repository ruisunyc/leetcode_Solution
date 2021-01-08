class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        dp = [0]*n
        for i,j,k in bookings:
            dp[i-1]+=k
            if j!=n:
                dp[j]-=k
        for i in range(1,n):
            dp[i]+=dp[i-1]
        return dp