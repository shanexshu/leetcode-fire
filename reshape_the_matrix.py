class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m*n != r*c: return mat
        
        ans = [[0]*c for _ in range(r)]
        
        row = col = 0
        for i in range(m):
            for j in range(n):
                ans[row][col] = mat[i][j]
                col = (col + 1) % c
                if col==0:
                    row += 1
        
        return ans