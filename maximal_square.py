class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m,n = len(matrix), len(matrix[0])
        dp = [[0]*n for _ in range(m)]
        biggest = 0
        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    dp[i][j] = int(matrix[i][j])
                else:
                    dp[i][j] = int(matrix[i][j]) * (min(dp[i-1][j-1],
                                                 dp[i][j-1],
                                                 dp[i-1][j]) + 1)
                biggest = max(biggest, dp[i][j])

        return biggest * biggest