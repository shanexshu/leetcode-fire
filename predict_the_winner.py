class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        def score(start, end, player):
            # returns: [player1_score, player2_score]
            
            # base case
            if start==end:
                # give the single value to the current player
                scores = [0,0]
                scores[player] = nums[start]
                return scores
            # general case
            
            # case 1: choose the first number
            # the next player gets to choose from nums[start+1:end]
            choice = nums[start]
            next_scores = score(start+1, end, (player+1)%2)
            next_scores[player] += choice
            ans = next_scores[:]
            
            # case 2: choose the last number
            choice = nums[end]
            next_scores = score(start, end-1, (player+1)%2)
            next_scores[player] += choice
            
            if next_scores[player] > ans[player]:
                ans = next_scores[:]
            
            return ans
        
        s1, s2 = score(0, len(nums)-1, 0)
        return s1>=s2
        
'''
1,3,7,5




'''