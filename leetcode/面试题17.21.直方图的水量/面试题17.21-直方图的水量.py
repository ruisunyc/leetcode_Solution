class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:return 0
        stack ,res = [],0
        for i in range(len(height)):
            while stack and height[stack[-1]]<height[i]:
                cur = stack.pop()
                if not stack:break
                res+=(min(height[stack[-1]],height[i])-height[cur])*(i-stack[-1]-1)
            stack.append(i) 
        return res