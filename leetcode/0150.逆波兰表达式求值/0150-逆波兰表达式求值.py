class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        d = {'/':lambda a,b:a/b,'*':lambda a,b:a*b,'+':lambda a,b:a+b,'-':lambda a,b:a-b}
        for num in tokens:
            if num not in '+-*/':stack.append(num)
            else:
                x1 = int(stack.pop())
                x2 = int(stack.pop())
                stack.append(d[num](x2,x1))
        return int(stack[0])
