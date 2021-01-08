class Solution:
    @lru_cache(None)
    def numRollsToTarget(self, d: int, f: int, target: int) -> int: 
        if d==1:
            if f>=target:return 1
            return 0
        count=0
        for i in range(1,f+1):
            if i<target:
                count += self.numRollsToTarget(d-1,f,target-i)
        return count%(10**9 + 7)
