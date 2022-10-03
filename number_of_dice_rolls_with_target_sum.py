class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MAX = 10**9 + 7
        
        dp = [[0] * (target+1) for _ in range(n+1)]
        
        dp[0][0] = 1
        
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                for f in range(1,k+1):
                    if 0<=j-f<len(dp[0]):
                        dp[i][j] += dp[i-1][j-f]
        
        return dp[-1][-1] % MAX
'''
dp

dp[i][j] = number of ways to get j from i dice

number of dice / target
 01234567
010000000
101111110   
200123456
30001
40
50
60

dp[i+1][j+1:j+k] = 

'''