class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_end_word = True

    def search(self, word: str) -> bool:
        to_visit = [self.root]
      
        for c in word:
            next_level = []
            for node in to_visit:
                if c == ".":
                    next_level.extend(node.children.values())
                if c in node.children:
                    next_level.append(node.children[c])
            to_visit = next_level
        
        for node in to_visit:
            if node.is_end_word:
                return True
            
        return False
