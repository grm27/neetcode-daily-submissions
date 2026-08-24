class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        char_word = defaultdict(str)
        word_char = defaultdict(str)
        words = s.split()

        if len(pattern) != len(words):
            return False

        for i in range(len(pattern)):
            char, word = pattern[i], words[i]
            if char not in char_word and word not in word_char:
                char_word[char] = word
                word_char[word] = char
            elif char_word[char] != word or word_char[word] != char:
                return False

        return True
