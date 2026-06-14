# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def bst_helper(node, low, high):
            if not node:
                return True
            
            if node.val <= low or node.val >= high:
                return False
            
            return bst_helper(node.left, low, min(high, node.val)) and bst_helper(node.right, max(low, node.val), high)
        
        return bst_helper(root, -float("inf"), float("inf"))