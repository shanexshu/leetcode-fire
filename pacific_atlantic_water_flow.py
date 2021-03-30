class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        pac_reachable = [[0]*n for _ in range(m)]
        atl_reachable = [[0]*n for _ in range(m)]
        
        def reach(i, j, table):
            if table[i][j]==0:
                table[i][j] = 1
                for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    i2, j2 = i+dx, j+dy
                    if 0<=i2<m and 0<=j2<n and matrix[i2][j2]>=matrix[i][j]:
                        reach(i2,j2,table)
        
        for i in range(m):
            reach(i, 0, pac_reachable)
            reach(i, n-1, atl_reachable)
        for j in range(n):
            reach(0, j, pac_reachable)
            reach(m-1, j, atl_reachable)
            
        ans = []
        for i in range(m):
            for j in range(n):
                if pac_reachable[i][j] and atl_reachable[i][j]:
                    ans.append([i, j])
        return ans