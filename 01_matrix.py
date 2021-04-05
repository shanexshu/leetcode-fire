class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]: return matrix
        m, n = len(matrix), len(matrix[0])
        dp = [[m+n]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    dp[i][j]=0
                else:
                    if i-1>=0:
                        dp[i][j] = min(dp[i][j], 1+dp[i-1][j])
                    if j-1>=0:
                        dp[i][j] = min(dp[i][j], 1+dp[i][j-1])
        
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if matrix[i][j]==0:
                    dp[i][j]=0
                else:
                    if i+1<m:
                        dp[i][j] = min(dp[i][j], 1+dp[i+1][j])
                    if j+1<n:
                        dp[i][j] = min(dp[i][j], 1+dp[i][j+1])
        
        return dp