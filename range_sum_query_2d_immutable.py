class NumMatrix:

    def __init__(self, matrix):
        self.matrix = matrix
        self.topleftsum = [[0]*len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i!=0 and j!=0:
                    self.topleftsum[i][j] = matrix[i][j] + self.topleftsum[i][j-1] + self.topleftsum[i-1][j] - self.topleftsum[i-1][j-1]
                else:
                    if i==j==0:
                        self.topleftsum[i][j] = matrix[i][j]
                    else:
                        if i==0:
                            self.topleftsum[i][j] = matrix[i][j] + self.topleftsum[i][j-1]
                        if j==0:
                            self.topleftsum[i][j] = matrix[i][j] + self.topleftsum[i-1][j]
                
    
    def sumRegion(self, row1, col1, row2, col2):
        leftcol = col1-1
        uprow = row1-1
        
        ans = self.topleftsum[row2][col2]
        if leftcol>=0:
            ans -= self.topleftsum[row2][leftcol]
        if uprow>=0:
            ans -= self.topleftsum[uprow][col2]
        if leftcol>=0 and uprow>=0:
            ans += self.topleftsum[uprow][leftcol]
        
        return ans

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)