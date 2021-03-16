class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n==0: return 0
        dpleft = [height[0]]*n
        dpright = [height[-1]]*n
        ans = 0
        for i in range(1, n):
            dpleft[i] = max(height[i], dpleft[i-1])
        for i in range(n-2,-1,-1):
            dpright[i] = max(height[i], dpright[i+1])
        for i in range(n):
            ans += min(dpleft[i], dpright[i]) - height[i]
        return ans