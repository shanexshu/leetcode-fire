class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n<2: return k
        dp = [0]*n
        dp[0] = k
        dp[1] = k*k
        for i in range(2, n):
            dp[i] = (dp[i-2]+dp[i-1]) * (k-1)
            
        return dp[-1]