"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        q_ancestors = set()

        node = q
        while node:
            q_ancestors.add(node)
            node = node.parent
        
        node = p
        while node:
            if node in q_ancestors:
                return node
            node = node.parent