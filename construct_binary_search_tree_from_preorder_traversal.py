# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        node = root
        i = 1
            
        def dfs(node, mn, mx):
            nonlocal i
            if i == len(preorder):
                return
            if mn < preorder[i] < node.val:
                node.left = TreeNode(preorder[i])
                i += 1
                dfs(node.left, mn, node.val)
            if i == len(preorder):
                return
            if node.val < preorder[i] < mx:
                node.right = TreeNode(preorder[i])
                i += 1
                dfs(node.right, node.val, mx)
        
        dfs(node, -math.inf, math.inf)
        
        return root