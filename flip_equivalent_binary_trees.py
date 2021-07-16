# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        
        def equiv(root1, root2):
            if root1 and root2:
                return root1.val==root2.val
            if not root1 and not root2:
                return True
            return False
        
        if not root1 and not root2: 
            return True
        if not root1 or not root2:
            return False
        
        if root1.val != root2.val:
            return False
        
        left1, left2 = root1.left, root2.left
        right1, right2 = root1.right, root2.right
        if not equiv(left1, left2):
            left1, right1 = root1.right, root1.left 
        
        return self.flipEquiv(left1, left2) and self.flipEquiv(right1, right2)
    
    