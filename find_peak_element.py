import math
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # use binary search to look for the highest value
        
        left = 1
        right = len(nums)
        
        padded = [-math.inf] + nums + [-math.inf]
        
        while left<=right:
            mid = (left+right)//2
            if padded[mid-1]<padded[mid] and padded[mid+1]<padded[mid]:
                return mid-1
            if padded[mid-1]>=padded[mid]:
                right = mid-1
            else:
                left = mid+1
        
        return 0