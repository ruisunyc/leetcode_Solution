class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:return []
        q = deque([])        
        ans = []
        for i in range(len(nums)): 
            if q and i-q[0]>=k:
                q.popleft()
            while q and nums[q[-1]]<=nums[i]:
                q.pop()            
            q.append(i)
            if q[-1]>=k-1:
                ans.append(nums[q[0]])
        return ans