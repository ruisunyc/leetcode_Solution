class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        two,one = 0 ,0
        for num in nums:
            one = one ^num & (~two)
            two = two ^ num & (~one)
        return one