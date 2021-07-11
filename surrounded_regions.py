class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        # dfs from Os on the border
        # mark those all visited
        # loop through inside
        # for each O, if not visited, turn into X
        
        def dfs(x, y):
            if not visited[x][y] and board[x][y]=='O':
                visited[x][y] = 1
                for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                    x2, y2 = x+dx, y+dy
                    if 0<=x2<m and 0<=y2<n:
                        dfs(x2,y2)
                
        m, n = len(board), len(board[0])
        visited = [[0]*n for _ in range(m)]
        for i in range(1, m-1):
            dfs(i, 0)
            dfs(i, n-1)
        for j in range(1, n-1):
            dfs(0, j)
            dfs(m-1, j)
            
        for i in range(1, m-1):
            for j in range(1, n-1):
                if board[i][j]=='O' and visited[i][j]==0:
                    board[i][j] = 'X'
                    
        