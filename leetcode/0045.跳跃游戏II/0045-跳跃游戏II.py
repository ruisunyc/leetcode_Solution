class Solution:
    def jump(self,nums:List[int])->int:
        maxpos=end=ans=0
        for i in range(len(nums)-1):
            maxpos = max(maxpos,i+nums[i])
            if i==end:
                ans+=1
                end=maxpos
        return ans