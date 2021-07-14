class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n==0: return 0
        left_max = [height[0]]*n
        right_max = [height[-1]]*n
        ans = 0
        
        for i in range(1, n):
            left_max[i] = max(height[i], left_max[i-1])
        
        for i in reversed(range(0, n-1)):
            right_max[i] = max(height[i], right_max[i+1])
        
        for i in range(n):
            ans += min(left_max[i], right_max[i]) - height[i]
        
        return ans