class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        time = 0
        todo = deque()
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    todo.append((i,j, 0))
                if grid[i][j]==1:
                    fresh += 1
        while todo:
            x, y, time = todo.popleft()
            for dx,dy in [(0,1),(0,-1),(-1,0),(1,0)]:
                x2, y2 = x+dx, y+dy
                if 0<=x2<m and 0<=y2<n and grid[x2][y2]==1:
                    todo.append((x2, y2, time+1))
                    grid[x2][y2] = 2
                    fresh -= 1
                        
        if fresh>0: return -1
        return time
        