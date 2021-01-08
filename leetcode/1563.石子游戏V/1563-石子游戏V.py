class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        # presum=[stoneValue[0]]
        # for i in range(1,len(stoneValue)):
        #     presum.append(stoneValue[i]+presum[-1])
        
        # @lru_cache(None)
        # def dfs(left,right):
        #     if left>=right: return 0
        #     ans = 0
        #     allsum = presum[right]-presum[left-1] if left>0 else presum[right]
        #     for i in range(left,right):
        #         suml = presum[i]-presum[left-1] if left>0 else presum[i]
        #         sumr = allsum - suml
        #         if suml<sumr:                  
        #             ans = max(ans,dfs(left,i)+suml)                   
        #         elif suml>sumr:
        #             ans =max(ans,dfs(i+1,right)+sumr)
        #         else:
        #             ans = max(ans,dfs(left,i)+suml,dfs(i+1,right)+sumr)
        #     return ans          
        # return dfs(0,len(presum)-1)
        @lru_cache(None)
        def dfs(left: int, right: int) -> int:
            if left == right:
                return 0
            
            total = sum(stoneValue[left:right+1])
            suml = ans = 0
            for i in range(left, right):
                suml += stoneValue[i]
                sumr = total - suml
                if suml < sumr:
                    ans = max(ans, dfs(left, i) + suml)
                elif suml > sumr:
                    ans = max(ans, dfs(i + 1, right) + sumr)
                else:
                    ans = max(ans, max(dfs(left, i), dfs(i + 1, right)) + suml)
            return ans
        
        n = len(stoneValue)
        return dfs(0, n - 1)
