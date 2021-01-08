class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:return 0
        amin = amax = res = nums[0]
        for i in range(1,len(nums)):
            cur = (amin*nums[i],amax*nums[i],nums[i])
            amin = min(cur)
            amax = max(cur)
            res = max(res,amax)
        return res