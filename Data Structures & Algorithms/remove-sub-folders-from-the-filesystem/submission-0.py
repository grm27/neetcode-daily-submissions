class TrieNode:
    def __init__(self, is_end=False):
        self.children = {}
        self.is_end = is_end


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        res = []
        root = TrieNode()
        folder.sort()

        for f in folder:
            curr_node = root
            is_sub = False
            for c in f:
                if c not in curr_node.children:
                    curr_node.children[c] = TrieNode()
                curr_node = curr_node.children[c]
                if curr_node.is_end:
                    is_sub = True
                    break
            curr_node.children["/"] = TrieNode(True)
            if not is_sub:
                res.append(f)

        return res
