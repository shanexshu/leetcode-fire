class TicTacToe:

    def __init__(self, n: int):

        self.rowsums = [0]*n
        self.colsums = [0]*n
        self.diagsums = [0]*2
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:

        val = [0,1,-1]

        self.rowsums[row] += val[player]
        self.colsums[col] += val[player]
        if row==col:
            self.diagsums[0] += val[player]
        if row==self.n-col-1:
            self.diagsums[1] += val[player]
        
        totals = [self.rowsums[row], self.colsums[col], self.diagsums[0], self.diagsums[1]]

        if self.n in totals:
            return 1
        if -self.n in totals:
            return 2
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)