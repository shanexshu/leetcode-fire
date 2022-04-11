class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m,n = len(grid), len(grid[0])
        ans = [[0]*n for _ in range(m)]
        
        shift = k % (m*n)
        if shift == 0: return grid
        rows = shift // n
        cols = shift % n
        
        for i in range(m):
            for j in range(n):
                sourceCol = j-cols
                sourceRow = i-rows
                if sourceCol < 0:
                    sourceRow -= 1
                sourceRow %= m
                sourceCol %= n
                ans[i][j] = grid[sourceRow][sourceCol]
                
        return ans