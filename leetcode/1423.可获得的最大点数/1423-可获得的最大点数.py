class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        pre = ans = sum(cardPoints[:k])
        for i in range(k-1,-1,-1):
            pre = pre - cardPoints[i]+cardPoints[i-k]
            ans = max(ans,pre)
        return ans
