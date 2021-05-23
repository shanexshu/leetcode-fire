class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        board = [["."]*n for _ in range(n)]
        ans = []
        
        def isValid(row, col):
            
            for j in range(col):
                # check rows
                if board[row][j] == 'Q': return False
            
            for i in range(row):
                # check col
                if board[i][col] == 'Q': return False
                
                # check diags
                if 0<=col-row+i<n and board[i][col-row+i] == 'Q': return False
                if 0<=col+row-i<n and board[i][col+row-i] == 'Q': return False
            
            return True
        
        def backtrack(row):
            nonlocal ans
            nonlocal board
            if row==n: 
                ans.append(["".join(board[row]) for row in range(n)])
                return
            for col in range(n):
                if isValid(row, col):
                    board[row][col] = "Q"
                    backtrack(row + 1)
                    board[row][col] = "."
                    
        backtrack(0)
        return ans
                