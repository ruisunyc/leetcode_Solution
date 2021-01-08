class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indgree = [0]*numCourses
        outdgree = [[] for _ in range(numCourses)]
        for x,y in prerequisites:
            indgree[x]+=1
            outdgree[y].append(x)
        q = collections.deque([x for x in range(numCourses) if not indgree[x]])
        while q:
            x = q.popleft()
            numCourses-=1
            for y in outdgree[x]:
                indgree[y]-=1
                if not indgree[y]:
                    q.append(y)
        return not numCourses