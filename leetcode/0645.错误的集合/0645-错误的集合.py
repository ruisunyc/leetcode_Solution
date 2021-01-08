class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:        
        for num in nums:
            cur = abs(num)
            if nums[cur-1]<0:
                dup = cur                           
            else:
                nums[cur-1]*=-1
        for i,num in enumerate(nums):
            if num>0:
                mis = i+1
                break
        return [dup,mis]
