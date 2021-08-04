# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        
        ans = []
        
        def findPath(node, path, currSum):
            nonlocal ans
            if node:
                s = currSum + node.val
                p = path + [node.val]
                if s == targetSum and not node.left and not node.right:
                    ans.append(p)
                else:
                    findPath(node.left, p, s)
                    findPath(node.right, p, s)
                    
        findPath(root, [], 0)
        return ans