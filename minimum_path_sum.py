import math
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        dp = [[math.inf]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i==j==0:
                    dp[i][j] = grid[i][j]
                else:
                    if i!=0:
                        dp[i][j] = min(dp[i][j], dp[i-1][j]+grid[i][j])
                    if j!=0:
                        dp[i][j] = min(dp[i][j], dp[i][j-1]+grid[i][j])
        
        return dp[-1][-1]