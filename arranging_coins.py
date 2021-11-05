class Solution:
    def arrangeCoins(self, n: int) -> int:
        lower_bound = n**0.5
        upper_bound = 2*lower_bound
        ans = 0
        for k in range(int(lower_bound), int(upper_bound)+1):
            if k*(k+1) <= 2*n:
                ans = k
                
        return ans