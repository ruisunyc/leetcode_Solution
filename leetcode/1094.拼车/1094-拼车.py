class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        d = [0]*1001
        for c,i,j in trips:
            d[i]+=c
            d[j]-=c
        for i in range(1,1001):
            d[i]+=d[i-1]
            if d[i]>capacity:return False
        return True