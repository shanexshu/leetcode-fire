# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            
            if not node: return -1, -1
            left_height, left_longest = dfs(node.left)
            right_height, right_longest = dfs(node.right)
            long_path = left_height + right_height + 2
            
            ret = max(left_height+1, right_height+1), max(left_longest, right_longest, long_path)
            return ret
        
        return dfs(root)[1]
                