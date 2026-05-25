class Solution:
    def firstUniqChar(self, s: str) -> int:
        index_dict = [-1] * 26
        is_unique = [True] * len(s)

        for i in range(len(s)):
            char_index = ord(s[i]) - ord("a")
            if index_dict[char_index] != -1:
                is_unique[index_dict[char_index]] = False
                is_unique[i] = False
            else:
                index_dict[char_index] = i
        
        for i in range(len(s)):
            if is_unique[i]:
                return i
        
        return -1
