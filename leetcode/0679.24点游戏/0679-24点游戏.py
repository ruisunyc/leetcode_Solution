class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        if not nums:return False
        def dfs(nums):
            if len(nums)==1:return abs(nums[0]-24)<=1e-5
            for i in range(len(nums)):
                for j in range(i+1,len(nums)):
                       last = [nums[k] for k in range(len(nums)) if k!=i and k!=j]
                       if dfs(last+[nums[i]+nums[j]]):return True 
                       if dfs(last+[nums[i]*nums[j]]):return True
                       if dfs(last+[nums[i]-nums[j]]):return True
                       if dfs(last+[-nums[i]+nums[j]]):return True
                       if (nums[j] and dfs(last+[nums[i]/nums[j]])):return True
                       if (nums[i] and dfs(last+[nums[j]/nums[i]])):return True
        return dfs(nums)
