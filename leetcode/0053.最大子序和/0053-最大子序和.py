class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:return 0
        cur = ans = nums[0]
        for i in range(1,len(nums)):
            cur = max(nums[i],cur+nums[i])
            ans = max(ans,cur)
        return ans