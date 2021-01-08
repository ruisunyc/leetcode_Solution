class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i,j = 0,0
        ans = []
        while i<len(A) and j<len(B):
            left = max(A[i][0],B[j][0])
            right = min(A[i][1],B[j][1])
            if left<=right:ans.append([left,right])
            if A[i][1]<=B[j][1]:i+=1                
            else:j+=1
        return ans