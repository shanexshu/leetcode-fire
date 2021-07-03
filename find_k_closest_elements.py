import math

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # idea: use binary search to look for x
        # from ending point, expand to each side until k closest numbers found
        
        left = 0
        right = len(arr)-1
        while right>=left:
            mid = (left+right)//2
            if arr[mid]==x:
                break
            if arr[mid]>x:
                right = mid-1
            else:
                left = mid + 1
        
        # if x not found, right<x<left
        
        if arr[mid]==x:
            right = mid
            left = mid+1
            
        ans = []
        for i in range(k):
            diff_right, diff_left = math.inf, math.inf
            
            if right>=0: 
                diff_right = abs(arr[right]-x)
            if left<len(arr): 
                diff_left = abs(arr[left]-x)
            if diff_right<=diff_left:
                ans.append(arr[right])
                right -= 1
            else:
                ans.append(arr[left])
                left += 1
            
        return sorted(ans)