class Solution:
    def minFlips(self, target: str) -> int:
        # target = '0'+target
        # res = 0
        # for i in range(1,len(target)):
        #     if target[i]!=target[i-1]:
        #         res+=1
        # return res
        res,pre = 0,'0'
        for num in target:
            if num!=pre:
                pre = num
                res+=1
        return res