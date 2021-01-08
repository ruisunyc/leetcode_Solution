class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a = b = float('inf')
        for num in nums:                
            if num<=a:
                a=num
            elif num<=b:
                b=num 
            elif num>b:
                return True
        return  False