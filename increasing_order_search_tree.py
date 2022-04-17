# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.newTree = None
        self.newNode = None
        
        def dfs(node):
            if node:
                dfs(node.left)
                if not self.newNode:
                    self.newTree = TreeNode(node.val)
                    self.newNode = self.newTree
                else:
                    self.newNode.right = TreeNode(node.val)
                    self.newNode = self.newNode.right
                dfs(node.right)
        
        dfs(root)
        return self.newTree