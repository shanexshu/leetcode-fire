"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        
        q = deque()
        q.append(root)
        
        while q:
            node = q.popleft()
            if node:
                ans.append(node.val)
                for c in reversed(node.children):
                    q.appendleft(c)
        
        return ans