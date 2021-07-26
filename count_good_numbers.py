class Solution:
    def countGoodNumbers(self, n: int) -> int:
        odds = n//2
        ans = pow(20, odds, int(1e9)+7)
        if n%2:
            ans *= 5
        return ans % (int(1e9)+7)
        
'''
4
0000

0 -> 2, 4, 6, 8, 0
1 -> 2, 3, 5, 7
'''