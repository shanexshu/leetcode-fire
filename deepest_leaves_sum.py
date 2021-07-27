# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        q = deque()
        q.append([root,0])
        curr = 0
        ans = 0
        while q:
            node,d = q.popleft()
            if node:
                if d>curr: 
                    curr = d
                    ans = 0
                ans += node.val
                q.append([node.left, d+1])
                q.append([node.right, d+1])
        
        return ans
'''
     6
    7 8
  2 7 1 3
9  1 4   5
'''