class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sets =set()
        i=-1
        ans = 0
        for j in range(len(s)):
            while s[j] in sets:
                i+=1
                sets.remove(s[i])
            sets.add(s[j])
            ans = max(ans,j-i)
        return ans