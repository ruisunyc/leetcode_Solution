class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(nums,tmp):
            if len(tmp)>1:res.append(tmp)
            vis = set()
            for i in range(len(nums)):
                if nums[i] in vis:continue
                vis.add(nums[i])
                if not tmp or  nums[i]>=tmp[-1]:
                    dfs(nums[i+1:],tmp+[nums[i]])
        dfs(nums,[])
        return res