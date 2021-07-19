# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        
        #      1
        #    2   3
        #   4 5
        #
        #	 1
        #    2   3
        #   4 5

        # root = left
        # left = right
        # right = root

        def helper(node):
            if node:
                if node.left:
                    nextnode = node.left
                    leftmost = helper(nextnode)
                    nextnode.right, nextnode.left = node, node.right
                    node.right = None
                    node.left = None
                    return leftmost
                else:
                    return node

        return helper(root)
