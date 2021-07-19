from collections import deque
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        # max: m+n-1
        # min: 0
        # max dist from i, j to i2, j2 is (i2-i)+(j2-j)
        m, n = len(grid), len(grid[0])
        
        q = deque()
        q.append((0,0,0))
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = [[0]*n for _ in range(m)]
        while q:
            i, j, changes = q.popleft()
            visited[i][j] = 1
            if i==m-1 and j==n-1:
                return changes
            sign = grid[i][j]
            for d in range(4):
                i2, j2 = i+dirs[d][0], j+dirs[d][1]
                if 0<=i2<m and 0<=j2<n and not visited[i2][j2]:
                    if d+1 == sign:
                        q.appendleft((i2,j2,changes))
                    else:
                        q.append((i2,j2,changes+1))
        
        return m+n-1