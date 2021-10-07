class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board), len(board[0])
        
        def dfs(word_i, row, col):
            
            if word_i==len(word):
                return True
            if 0<=row<m and 0<=col<n and v[row][col]==0:
                if board[row][col]!=word[word_i]:
                    return False
                v[row][col] = 1
                for drow, dcol in [(1,0),(0,1),(-1,0),(0,-1)]:
                    if dfs(word_i+1, row+drow, col+dcol):
                        return True
                v[row][col] = 0
            return False
        
        v = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if dfs(0,i,j):
                    return True
        return False