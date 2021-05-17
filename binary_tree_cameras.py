# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.ans = 0
        self.covered = set()
        self.covered.add(None)
        
        def dfs(node, parent):
            if node: 
                
                dfs(node.left, node)
                dfs(node.right, node)
                
                if (parent is None and node not in self.covered) or \
                (node.left not in self.covered or node.right not in self.covered):
                    self.ans += 1
                    self.covered.update([node, node.left, node.right, parent])
                        
        dfs(root, None)
        return self.ans
                