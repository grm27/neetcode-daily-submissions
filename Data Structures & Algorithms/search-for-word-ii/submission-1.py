class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end_word = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        root = TrieNode()
        for word in words:
            self._insertWord(root, word)
        
        deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        res = []
        def dfs(i, j, curr_node, curr_word, visited):
            if i < 0 or j < 0 or i == m or j == n or (i, j) in visited:
                return
            
            curr_char = board[i][j]
            if curr_char not in curr_node.children:
                return
            
            visited.add((i, j))
            curr_node = curr_node.children[curr_char]
            if curr_node.is_end_word:
                res.append(curr_word + curr_char)
                curr_node.is_end_word = False
            
            for dx, dy in deltas:
                dfs(i + dx, j + dy, curr_node, curr_word + curr_char, visited)
            visited.remove((i, j))
        
        for i in range(m):
            for j in range(n):
                dfs(i, j, root, "", set())
        
        return res


    def _insertWord(self, root, word):
        curr = root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_end_word = True