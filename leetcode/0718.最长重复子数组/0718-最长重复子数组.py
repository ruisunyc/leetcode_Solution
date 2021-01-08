class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        if len(A)>len(B):
            A,B = B,A
        ans = []
        for i in range(len(A)):
            cur = A[i-len(ans):i+1]
            for j in range(len(B)-len(cur)+1):
                if B[j:j+len(cur)]==cur:
                    ans = cur
                    break
        # print(ans)
        return len(ans)