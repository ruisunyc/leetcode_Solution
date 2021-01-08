class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cur = None
        count = 0
        for num in nums:    
            if count==0:
                cur=num          
            if cur!=num:
                count-=1
            else:
                count+=1
        return cur