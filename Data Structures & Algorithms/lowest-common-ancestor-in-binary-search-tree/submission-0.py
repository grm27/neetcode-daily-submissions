# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        p_path = set([root])

        node = root
        while node.val != p.val:
            if p.val < node.val:
                node = node.left
            else:
                node = node.right
            p_path.add(node)

        res = root
        node = root
        while node.val != q.val:
            if q.val < node.val:
                node = node.left
            else:
                node = node.right
            if node in p_path:
                res = node

        return res
