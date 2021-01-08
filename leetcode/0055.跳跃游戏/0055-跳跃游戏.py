class Solution:
    def canJump(self,nums:List[int])->bool:
        n = len(nums)
        maxpos = 0
        for i in range(n):
            if maxpos>=i:
                maxpos = max(maxpos,i+nums[i])
                if maxpos>=n-1:
                    return True
        return False