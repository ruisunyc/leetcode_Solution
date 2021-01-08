class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack  = []
        for num in arr:
            if stack and num<stack[-1]:
                cur = stack.pop()
                while stack and num<stack[-1]:
                    stack.pop()
                stack.append(cur)
            else:
                stack.append(num)
        return len(stack)
        # for num in arr:
        #     while len(stack)>=2 and num<stack[-2]:
        #         stack.pop(-2)
        #     if not stack or num>=stack[-1]:
        #         stack.append(num)
        # return len(stack)
