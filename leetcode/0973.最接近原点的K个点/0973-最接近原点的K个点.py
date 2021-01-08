class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        ans = [(i**2+j**2,ind) for ind,(i,j) in enumerate(points)]
        print(ans)
        # return [points[i] for  va,i in sorted(ans,key=lambda x:x[0])[:K]]
        heapq.heapify(ans)
        return [points[heapq.heappop(ans)[1]] for _ in range(K)]