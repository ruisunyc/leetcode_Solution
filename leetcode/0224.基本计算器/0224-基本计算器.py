class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ','')        
        def dfs(s):
            sign = '+'
            stack = []
            num=0
            while s:
                cur = s.popleft()  
                if cur=='(':
                    num = dfs(s)  
                if cur.isdigit():
                    num = num*10+int(cur) 
                if not s or not cur.isdigit():
                    if sign=='+':
                        stack.append(num)
                    elif sign=='-':
                        stack.append(-num)
                    num=0
                    sign = cur
                if cur==')':break
            return sum(stack)
        return dfs(deque(list(s)))
       