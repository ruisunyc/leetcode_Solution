class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        #当前最大值与当前位置相对即满足时刻
        cur = light[0]
        ans = 0
        for i,num in enumerate(light):
            cur = max(cur,num)
            if cur==i+1:
                ans+=1
        return ans