# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        
        def add(node):
            ans = 0
            if node:
                if low<=node.val<=high:
                    ans += node.val
                ans += add(node.left) + add(node.right)
            return ans
        
        return add(root)
            