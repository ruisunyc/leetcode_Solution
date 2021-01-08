class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        s = [0]*(len(A)+1)
        for i in range(1,len(s)):
            s[i]=s[i-1]+A[i-1]
        ans = 0
        for i in range(2):            
            Lmax = 0
            for j in range(L,len(s)-M):
                Lmax = max(Lmax,s[j]-s[j-L])
                ans = max(ans,Lmax+s[j+M]-s[j])
            if L==M:break
            L,M = M,L
        return ans
