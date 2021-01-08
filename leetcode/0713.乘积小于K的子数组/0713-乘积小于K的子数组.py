class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:return 0
        ans = 0
        prod = 1
        left=-1
        for i in range(len(nums)):
            prod*=nums[i]
            while  prod>=k:
                left+=1
                prod/=nums[left]
            ans+=i-left
        return ans
            