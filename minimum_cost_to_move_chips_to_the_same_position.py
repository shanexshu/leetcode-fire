class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odds = 0
        evens = 0
        for num in position:
            if num%2==0:
                evens += 1
            else:
                odds += 1
                
        return min(odds,evens)