class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        
        def dp(i, j, min_path=(0,0)):
            if (i, j) in memo:
                return memo[(i, j)]
            if i<m and j<n:
                cur_path = dungeon[i][j]
                right = max(1, dp(i, j+1, cur_path) - cur_path)
                down = max(1, dp(i+1, j, cur_path) - cur_path)
                
                ret = min(right, down)
                
                if ret == float('inf'):
                    if cur_path >= 0:
                        ret = 1
                    else:
                        ret = 1 - cur_path
                    
                memo[(i, j)] = ret
                return ret
            else:
                return float('inf')
            
        m = len(dungeon)
        n = len(dungeon[0])
        memo = {}
        return dp(0, 0)