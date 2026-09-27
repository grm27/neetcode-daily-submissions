# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        final = False

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    if final:
                        return False
                    queue.append(node.left)
                else:
                    final = True

                if node.right:
                    if final:
                        return False
                    queue.append(node.right)
                else:
                    final = True

        return True
