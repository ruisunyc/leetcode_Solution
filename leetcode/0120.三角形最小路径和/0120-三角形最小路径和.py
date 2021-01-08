class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:return 0
        for i in range(1,len(triangle)):
            for j in range(len(triangle[i])):
                if j==0:
                    triangle[i][j] +=triangle[i-1][0]
                elif j==i:
                    triangle[i][j] +=triangle[i-1][j-1]
                else:
                    triangle[i][j]+=min(triangle[i-1][j-1],triangle[i-1][j])
        return min(triangle[-1] )
