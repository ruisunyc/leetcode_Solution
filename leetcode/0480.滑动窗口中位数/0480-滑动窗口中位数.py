class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        arr,left,ans = [],0,[]
        for i in range(len(nums)):
            bisect.insort_left(arr,nums[i])
            if len(arr)>k:
                arr.pop(bisect.bisect_left(arr,nums[left]))
                left+=1
            if len(arr)==k:
                ans.append((arr[k//2]+arr[(k-1)//2])/2)
        return ans