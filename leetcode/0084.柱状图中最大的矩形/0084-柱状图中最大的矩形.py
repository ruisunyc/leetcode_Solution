class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #µ¥µ÷ÔöÕ»+Ë«¶ËÉÚ±ø
        heights=[0]+heights+[0]
        stack=[0]
        ans = 0
        for i in range(1,len(heights)):
            while heights[stack[-1]]>heights[i]:
                h = heights[stack.pop()]
                w = i-stack[-1]-1
                ans = max(ans,h*w)
            stack.append(i)
        return ans