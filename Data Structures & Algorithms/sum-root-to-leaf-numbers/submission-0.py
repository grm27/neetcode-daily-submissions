# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        nums = []

        def num_helper(node, curr_num):
            if not node:
                return
            
            if not node.left and not node.right:
                nums.append(curr_num * 10 + node.val)
                return
            
            num_helper(node.left, curr_num * 10 + node.val)
            num_helper(node.right, curr_num * 10 + node.val)

        num_helper(root, 0)

        return sum(nums)            
