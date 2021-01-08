class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n<=2:return 0
        stack = []
        ans = 0
        for i,num in enumerate(height):
            while stack and height[stack[-1]]<num:
                cur = stack.pop()
                if stack:
                    ans+=(min(height[stack[-1]],num)-height[cur])*(i-stack[-1]-1)
            stack.append(i)
        return ans
