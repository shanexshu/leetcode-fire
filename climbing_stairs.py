class Solution:
    def climbStairs(self, n: int) -> int:
        if n<3: return n
        n1, n2 = 1, 2
        for i in range(3, n+1):
            n1, n2 = n2, n2 + n1
        return n2