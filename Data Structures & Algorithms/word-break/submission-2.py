class TrieNode:

    def __init__(self):
        self.children = [None] * 26
        self.is_end = False


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {}

        root = self.init(wordDict)

        def dfs(i):
            if i in cache:
                return cache[i]

            if i == len(s):
                return True

            node = root
            for j in range(i, len(s)):
                char_idx = ord(s[j]) - ord("a")
                if not node.children[char_idx]:
                    cache[i] = False
                    return cache[i]

                node = node.children[char_idx]
                if node.is_end and dfs(j + 1):
                    cache[i] = True
                    return cache[i]

            cache[i] = False
            return cache[i]

        return dfs(0)

    def init(self, wordDict):
        root = TrieNode()

        for word in wordDict:
            node = root
            for c in word:
                char_idx = ord(c) - ord("a")
                if not node.children[char_idx]:
                    node.children[char_idx] = TrieNode()
                node = node.children[char_idx]
            node.is_end = True

        return root
