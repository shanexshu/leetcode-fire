class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0: return False
        threes = [3**i for i in range(30) if 3**i<2**31]
        if n in threes:
            return True
        return False