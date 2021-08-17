# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0
        
        def dfs(node, pathmax=-math.inf):
            nonlocal good
            if node:
                if node.val >= pathmax:
                    good += 1
                    pathmax = max(pathmax, node.val)
                dfs(node.left, pathmax)
                dfs(node.right, pathmax)
        dfs(root)
        return good
        