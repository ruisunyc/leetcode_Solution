class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        d = defaultdict(set)
        n = len(beginWord)
        for num in wordList:
            for i in range(n):
                d[num[:i]+'_'+num[i+1:]].add(num)  
        q = deque([(beginWord,1)])
        vis = set()
        while q:
            cur,leng = q.popleft()
            for i in range(n):
                for word in d[cur[:i]+'_'+cur[i+1:]]: 
                    if word==endWord:
                        return leng+1
                    if word not in vis:
                        vis.add(cur)                        
                        q.append((word,leng+1))
            d[cur]=set()
        return 0