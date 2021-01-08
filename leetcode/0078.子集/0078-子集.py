class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # nums.sort()
        ans = []
        def dfs(nums,tmp):
            ans.append(tmp)
            for i in range(len(nums)):
                # if i>0 and nums[i-1]==nums[i]:continue
                dfs(nums[i+1:],tmp+[nums[i]])
        dfs(nums,[])
        return ans