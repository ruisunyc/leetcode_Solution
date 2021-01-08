class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        ans = 0
        l = []
        for num in nums[::-1]:
            ind = bisect.bisect_left(l,num)
            ans+=ind
            l.insert(ind,num)
        return ans