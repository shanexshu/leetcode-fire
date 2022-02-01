class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        dip = prices[0]
        for i in range(1,len(prices)):
            profit = max(profit, prices[i]-dip)
            dip = min(dip, prices[i])
        return profit