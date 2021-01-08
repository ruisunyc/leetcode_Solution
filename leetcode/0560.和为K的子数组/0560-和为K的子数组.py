class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {0:1}
        sums,ans = 0,0
        for num in nums:
            sums+=num
            if sums-k in d:
                ans+=d[sums-k]
            d[sums]=d.get(sums,0)+1
        return ans