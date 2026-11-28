# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        nodes = [root]
        children = []
        for node in nodes:
            ids = []
            for child in (node.left, node.right):
                if child:
                    ids.append(len(nodes))
                    nodes.append(child)
            children.append(ids)
        counts = [[0] * (distance + 1) for _ in nodes]
        answer = 0
        for u in range(len(nodes) - 1, -1, -1):
            if not children[u]:
                counts[u][0] = 1
            for child in children[u]:
                for i in range(distance + 1):
                    for j in range(distance - i):
                        answer += counts[u][i] * counts[child][j]
                for j in range(distance):
                    counts[u][j + 1] += counts[child][j]
        return answer
