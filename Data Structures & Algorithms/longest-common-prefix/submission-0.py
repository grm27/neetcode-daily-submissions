class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end_word = False

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        root = TrieNode()

        for s in strs:
            curr_node = root
            for c in s:
                if c not in curr_node.children:
                    curr_node.children[c] = TrieNode()
                curr_node = curr_node.children[c]
            curr_node.is_end_word = True
        
        lcp = ""
        curr_node = root

        while len(curr_node.children) == 1 and not curr_node.is_end_word:
            next_char = next(iter(curr_node.children))
            lcp += next_char
            curr_node = curr_node.children[next_char]
        
        return lcp
