# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        m,n = binaryMatrix.dimensions()
        ans = n
        for i in range(m):
            left, right = 0, n-1
            while left<=right:
                mid = (left+right)//2
                if binaryMatrix.get(i,mid) == 1:
                    right = mid - 1
                else:
                    left = mid + 1
            ans = min(ans, left)
        
        if ans == n: return -1
        return ans