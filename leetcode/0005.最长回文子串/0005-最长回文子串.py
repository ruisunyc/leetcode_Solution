class Solution:
    def longestPalindrome(self, s: str) -> str:

        ans = ''
        for i in range(len(s)):
            cur = s[max(0,i-len(ans)-1):i+1]
            if cur==cur[::-1]:
                ans = cur
            elif s[i-len(ans):i+1]==s[i-len(ans):i+1][::-1]:
                ans = s[i-len(ans):i+1]
        return ans