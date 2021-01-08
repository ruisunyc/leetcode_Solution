class Solution:
    def mySqrt(self, x: int) -> int:
        #x0**2-a+2*x0*(x-x0)=0
        #2xx0-x0**2-a=0
        #x = 0.5*x0+0.5(a/x0) = 0.5*(x0+a/x0)
        # if x<=1:return x
        # x0=1
        # while True:
        #     cur = 0.5*(x0+x/x0)
        #     if abs(cur-x0)<=1e-5:
        #         return int(cur)
        #     x0=cur
        if x<=1:return x
        l,r = 0,x
        while l<=r:
            mid = (l+r)/2
            cur = mid**2
            if abs(cur-x)<=1e-5:
                return int(mid)
            if cur>x:
                r=mid
            else:
                l=mid
        
