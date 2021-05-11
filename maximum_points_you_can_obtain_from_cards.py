class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        ans = 0
        n = len(cardPoints)
        if k>=len(cardPoints): return sum(cardPoints)
        
        leftsums = rightsums = cardPoints[:]
        leftsums = [0] + leftsums
        rightsums += [0]
        
        for i in range(1, k+1):
            leftsums[i] += leftsums[i-1]
        
        for i in range(n-2,n-k-2,-1):
            rightsums[i] += rightsums[i+1]
        
        for i in range(k+1):
            score = (leftsums[i]) + (rightsums[n-(k-i)])
            ans = max(ans, score)
        return ans