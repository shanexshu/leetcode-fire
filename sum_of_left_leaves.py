# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        self.ans = 0
        
        def dfs(node,left):
            if not node:
                return
            if not node.left and not node.right and left:
                self.ans += node.val
            dfs(node.left,1)
            dfs(node.right,0)
            
        dfs(root,0)
        return self.ans