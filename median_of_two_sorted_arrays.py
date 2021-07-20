import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # init a partition pointer p1, p2 to mid of each array
        # check if nums1[p1]<nums2[p2+1] and nums2[p2]<nums1[p1+1]
        # if not, move p1 and p2 based on direction in a binary-search fashion
        
        m, n = len(nums1), len(nums2)
        if not m:
            if n%2:
                return nums2[n//2]
            return (nums2[n//2] + nums2[n//2-1])/2
        if not n:
            if m%2:
                return nums1[m//2]
            return (nums1[m//2] + nums1[m//2-1])/2
        
        # partition 2 depends entirely on partition 1. will focus on partition 1
        left, right = -1, m
        
        # total: m+n
        # p1 is the index of last element to be on left partition of nums1
        # => p1+1 elements from nums1
        # => (m+n)//2-(p1+1) elements needed from nums2
        # => p2 = (m+n)//2 - (p1+1) - 1
        while left<=right:
            p1 = (left+right)//2
            p2 = (m+n)//2 - p1 - 2
            if p2>=n:
                left += 1
                continue
            if p2<-1:
                right -= 1
                continue
            rightmin1 = rightmin2 = math.inf
            if p1+1<m: rightmin1 = nums1[p1+1]
            if p2+1<n: rightmin2 = nums2[p2+1]
                
            leftmax1 = leftmax2 = -math.inf
            if p1>=0: leftmax1 = nums1[p1]
            if p2>=0: leftmax2 = nums2[p2]
            
            if leftmax1>rightmin2:
                # move p1 to the left
                right = p1-1
            elif leftmax2>rightmin1:
                # move p1 to the right
                left = p1+1
            else:
                break
        
        if (m+n)%2:
            # odd
            return min(rightmin1, rightmin2)
        else:
            return (max(leftmax1, leftmax2) + min(rightmin1, rightmin2))/2
        
        
        
'''
odd: return min(right part)
[1,3,6,8,12,13]  7  len = 6
     |
[2,3,4,5,67]     4  len = 5
   |
[1,2,3,3,4,5,6,8,12,13,67]  5
 1,3       |    6,8,12,13          
 2,3,4     5       67
 
even: return avg(max(left), min(right))
[1,3,6,8,12,13]  7
 |   
[2,3,4,67]     3.5
        |
[1,2,3,3,4,6,8,12,13,67]  5
 1,3      |    6,8,12,13          
 2,3,4            67
'''


'''
1,3
 |
l r

 2
|
'''
