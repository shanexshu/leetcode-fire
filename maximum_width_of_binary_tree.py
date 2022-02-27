# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 1
        
        # BFS
        
        currLevel = [(root,0)]
        while currLevel:
            nextLevel = []
            minIndex = currLevel[0][1]
            for node, index in currLevel:
                self.ans = max(self.ans, index-minIndex+1)
                if node.left:
                    nextLevel.append((node.left, index*2))
                if node.right:
                    nextLevel.append((node.right, index*2+1))
            currLevel = nextLevel
            
        return self.ans