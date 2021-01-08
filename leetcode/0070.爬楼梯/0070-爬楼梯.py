class Solution:
    def climbStairs(self, n: int) -> int:
        a = b = 1
        for i in range(2,n+1):
            a,b =b,a+b
        return b