class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        
        # boundaries
        left = 0
        right = n
        top = 0
        bottom = m
        
        output = []
        
        i, j = 0, 0
        
        while len(output) < m*n:
            # go right
            while left <= j < right:
                output.append(matrix[i][j])
                j += 1
            top += 1
            i += 1
            j -= 1
            
            if len(output) >= m*n: break
            # go down
            while top <= i < bottom:
                output.append(matrix[i][j])
                i += 1
            right -= 1
            j -= 1
            i -= 1
            
            if len(output) >= m*n: break
            # go left
            while left <= j < right:
                output.append(matrix[i][j])
                j -= 1
            bottom -= 1
            i -= 1
            j += 1
            
            if len(output) >= m*n: break
            # go up
            while top <= i < bottom:
                output.append(matrix[i][j])
                i -= 1
            left += 1
            j += 1
            i += 1
            
        return output
        
'''
[[1,2,3],[4,5,6],[7,8,9]]
[[1,2,3,4],
[5,6,7,8],
[9,10,11,12]]
'''

