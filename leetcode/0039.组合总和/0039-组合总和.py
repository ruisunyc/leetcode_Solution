class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ans = []
        def dfs(i,tmp,cur):
            if cur>target:return
            if cur==target:
                ans.append(tmp)
                return 
            for j in range(i,n):
                dfs(j,tmp+[candidates[j]],cur+candidates[j])
        dfs(0,[],0)
        return ans
