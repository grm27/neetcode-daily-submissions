class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = [0] * 26

        for c in chars:
            chars_count[ord(c) - ord("a")] += 1
        
        res = 0
        for word in words:
            word_chars_count = [0] * 26
            good = True
            for c in word:
                c_indx = ord(c) - ord("a")
                word_chars_count[c_indx] += 1
                if word_chars_count[c_indx] > chars_count[c_indx]:
                    good = False
                    break
            if good:
                res += len(word)
        
        return res
                