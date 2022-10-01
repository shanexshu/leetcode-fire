class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s)<2: return int(self.isValidLetter(s))
        
        waysToDecode = 0
        dp = [0]*len(s)
        dp[0] += self.isValidLetter(s[0])
        dp[1] += self.isValidLetter(s[:2]) + (dp[0] and self.isValidLetter(s[1]))
        
        for i in range(2, len(s)):
            if self.isValidLetter(s[i]):
                dp[i] += dp[i-1]
            if self.isValidLetter(s[i-1:i+1]):
                dp[i] += dp[i-2]
            
        return dp[-1]
            
    def isValidLetter(self, chars: str) -> bool:
        if not chars or chars[0] == '0': return False
        return 0 < int(chars) <= 26
        
        
'''
11106
i

  
dp[i] = how many ways to decode up to ith
dp = [1, 2, 3, 2, 2]
dp[i] = dp[i-1] (if s[i] is valid standalone) + dp[i-2] (if s[i-1:i] is valid)

1111211
12358

1
1,1 11
1,1,1 11,1 1,11
1,1,1,1 11,11 1,11,1, 11,1,1 1,1,11
'''