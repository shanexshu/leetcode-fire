class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        ans = 0
        dp = [1]*n
        
        # loop from left, then from right
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                dp[i] = dp[i-1]+1
        
        for i in reversed(range(n-1)):
            if ratings[i]>ratings[i+1]:
                dp[i] = max(dp[i], dp[i+1] + 1)
                
            ans += dp[i]
            
        return ans + dp[-1]