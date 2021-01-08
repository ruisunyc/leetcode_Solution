class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        # print(nums)
        for i in range(0,n-2):
            if i>0 and nums[i-1]==nums[i]:continue

            j=i+1
            k= n-1
            cur = -nums[i]
            while j<k:
                if nums[j]+nums[k]>cur:
                    k-=1
                elif nums[j]+nums[k]<cur:
                    j+=1
                else:
                    ans.append([nums[i],nums[j],nums[k]])
                    while k>j>0 and nums[j+1]==nums[j]:
                        j+=1
                    while k>j>0 and nums[k-1]==nums[k]:
                        k-=1
                    j+=1
                    k-=1
        return ans