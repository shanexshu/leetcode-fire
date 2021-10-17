# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        def dfs(node, cumSum):
            nonlocal ans
            if node:
                newCum = cumSum + node.val
                if newCum == targetSum:
                    ans += 1
                if newCum-targetSum in seen:
                    ans += seen[newCum-targetSum]
                seen[newCum] += 1
                dfs(node.left, newCum)
                dfs(node.right, newCum)
                seen[newCum] -= 1
        
        ans = 0
        seen = defaultdict(int)
        dfs(root, 0)
        return ans