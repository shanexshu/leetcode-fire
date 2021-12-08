# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def getSumAndAddToTilt(node):
            # returns: totalSum
            # calculates tilt and adds to total tilt (ans). no need to return it
            
            nonlocal ans
            
            if not node:
                return 0
            leftSum = getSumAndAddToTilt(node.left)
            rightSum = getSumAndAddToTilt(node.right)
            
            ans += abs(leftSum - rightSum)
            
            return leftSum + rightSum + node.val
        
        getSumAndAddToTilt(root)
        return ans