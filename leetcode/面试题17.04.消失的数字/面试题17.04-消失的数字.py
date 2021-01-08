class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i,num in enumerate(nums):
            res ^= i^num
        return res