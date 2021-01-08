class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans = 0
        n1 = len(num1)
        n2 = len(num2)
        if n1>n2:num1,num2 = num2,num1
        num1 = '0'*(len(num2)-len(num1))+num1
        pre = 0
        ans = ''
        for i in range(len(num2)-1,-1,-1):
            cur = int(num1[i])+int(num2[i])+pre
            ans = str(cur%10)+ans
            pre = cur//10
        return ('1' if pre else '') + ans