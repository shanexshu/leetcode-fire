class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        if len(nums)<2:
            return nums[0]
        
        while left<=right:
            if left == right: return nums[left]
            mid = (left+right)//2
            if nums[mid]<nums[right]:
                right = mid
            elif nums[mid]>=nums[right]:
                left = mid+1
        
        return left
'''

[3,4,0,1,2]
 l   r
   m
[1,2,3,4,5]
'''