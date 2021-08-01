class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        islands = defaultdict(int)
        counted = set()
        n = len(grid)
        
        def dfs(i, j, ID):
            if (i,j) not in counted:
                counted.add((i,j))
                islands[ID] += 1
                grid[i][j] = ID
                for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                    i2, j2 = i+di, j+dj
                    if 0<=i2<n and 0<=j2<n and grid[i2][j2]==1:
                        dfs(i2,j2,ID)
        
        ID = 2
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    dfs(i,j,ID)
                    ID += 1
        
        ans = 0
        if islands:
            ans = max(islands.values())
            
        for i in range(n):
            for j in range(n):
                if grid[i][j]==0:
                    curr = 1
                    seen = set()
                    for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                        i2, j2 = i+di, j+dj
                        if 0<=i2<n and 0<=j2<n and grid[i2][j2]>1 and grid[i2][j2] not in seen:
                            seen.add(grid[i2][j2])
                            curr += islands[grid[i2][j2]]
                    ans = max(curr, ans)
        return ans
    
        