class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        left, right = 0, n-1
        
        while left<right:
            minheight = min(height[left], height[right])
            area = (right-left)*minheight
            ans = max(ans, area)
            if minheight==height[left]:
                left += 1
            else:
                right -= 1
        
        return ans
    
'''
    [1,8,6,2,5,4,8,3,7]
       l             r
    minheight = 49
    ans = 8
  
    [4,3,2,1,4]
           l r
    minheight = 3
    ans = 16 
  
 '''