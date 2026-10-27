class Solution:
    def constructFromPrePost(
        self, preorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        if not postorder:
            return None

        root = TreeNode(postorder.pop())

        if postorder:
            right_index = preorder.index(postorder[-1])
            root.left = self.constructFromPrePost(
                preorder[1:right_index], postorder[: right_index - 1]
            )
            root.right = self.constructFromPrePost(
                preorder[right_index:], postorder[right_index - 1 :]
            )

        return root
