class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:return 0
        flag = 1
        if s[0]=='-' or s[0]=='+':
            if s[0]=='-':flag=-1            
            s = s[1:]       
        ans =0
        for num in s:
            if num.isdigit():
                ans = ans*10+int(num)
            else:break
        ans*=flag      
        return min(max(ans,-2**31),2**31-1)