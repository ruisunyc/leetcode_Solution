class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(reverse = True) #排序的作用是从后往前判断开始时间，并弹出它
        h = [] #优先队列，也可以说是小顶堆
        ans = 0
        for i in range(1,100001):  #直接用数据范围（当然也可以取events结束时间的最大值，还要再写循环不够简练）
            while events and events[-1][0]==i: #排序的作用
                heapq.heappush(h,events.pop()[1]) #弹出
            while h:
                cur = heapq.heappop(h)
                if cur>=i:
                    ans+=1 #一天只能参加一次
                    break
            if not events and not h:break #既没有新源，也没有旧源，直接结束
        return ans