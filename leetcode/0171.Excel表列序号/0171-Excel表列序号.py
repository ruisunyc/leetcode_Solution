class Solution:
    def titleToNumber(self, s: str) -> int:
        
        ans = 0
        for num in s:
            ans = ans*26+ord(num)-64
        return ans