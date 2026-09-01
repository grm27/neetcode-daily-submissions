# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        parent = {}

        def dfs(node, p):
            if not node:
                return

            parent[node] = p
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)

        p_path = set()

        node = p
        while node:
            p_path.add(node)
            node = parent[node]

        node = q
        while node:
            if node in p_path:
                return node
            node = parent[node]
