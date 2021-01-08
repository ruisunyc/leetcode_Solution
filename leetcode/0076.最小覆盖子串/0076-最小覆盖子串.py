class Solution:
    def minWindow(self, s: str, t: str) -> str:
       #关键点：Counter,判断v最大值是否<=0
        c  = collections.Counter(t)
        left = -1
        ans = ''
        count = len(t)
        for i,num in enumerate(s):
            if c[num]>0:
                count-=1           
            c[num]-=1                
            while count==0:
                if not ans or i-left<len(ans):ans = s[left+1:i+1]
                left+=1
                if c[s[left]]==0:
                    count+=1 
                c[s[left]]+=1
        return ans