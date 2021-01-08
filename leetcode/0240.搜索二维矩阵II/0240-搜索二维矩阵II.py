class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        i,j = row-1,0
        while i>=0 and j<col:
            if matrix[i][j]<target:
                j+=1
            elif matrix[i][j]>target:
                i-=1
            else:
                return True
        return False