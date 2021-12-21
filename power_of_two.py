class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0: return False
        
        # intuition: use bit manip and compare n and n-1
        # n = 16 = 10000
        # n = 15 = 01111
        # n & (n-1) = 0 (zeros out the rightmost bit)
        # now check if that is 0
        # n = 3 = 011
        #     2 = 010
        # n & (n-1) = 010
        
        return (n & (n-1)) == 0