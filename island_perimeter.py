class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        m,n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    ans += (i==0) + (j==0) + (i==m-1) + (j==n-1)
                    if i>0: ans += (grid[i-1][j]==0)
                    if i<m-1: ans += (grid[i+1][j]==0)
                    if j>0: ans += (grid[i][j-1]==0)
                    if j<n-1: ans += (grid[i][j+1]==0)
        return ans