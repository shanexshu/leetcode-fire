# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        
        while root and (root.val < low or root.val > high):
            if root.val<low:
                root = root.right
            elif root.val>high:
                root = root.left
        
        ans = TreeNode(-1)
        ans.right = root
        q = deque()
        q.append((root, ans))
        while q:
            node, parent = q.popleft()
            if node:
                if node.val<low:
                    parent.left = node.right
                    q.append((node.right, parent))
                elif node.val>high:
                    parent.right = node.left
                    q.append((node.left, parent))
                else:
                    q.append((node.left, node))
                    q.append((node.right, node))
                
        return ans.right