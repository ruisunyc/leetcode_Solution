class Solution:
    def decodeString(self, s: str) -> str:

        dight = 0
        ans = ''
        stack = []
        for e in s:
            if '0'<=e<='9':
                dight = dight*10+int(e)
            elif e=='[':                
                stack.append([dight,ans])
                dight=0                
                ans=''
            elif e==']':
                lastd,lasta = stack.pop()
                ans = lasta+lastd*ans                
            else:
                ans+=e 
        return ans
            