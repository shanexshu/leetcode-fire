class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid: return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if j>0:
                    dp[i][j] += dp[i][j-1]
                if i>0:
                    dp[i][j] += dp[i-1][j]
                dp[i][j] *= (1-obstacleGrid[i][j])
        return dp[-1][-1]
                    