class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = [0] * 26

        for i in range(len(s)):
            char_count[ord(s[i]) - ord("a")] += 1
        
        for i in range(len(s)):
            if char_count[ord(s[i]) - ord("a")] == 1:
                return i
        
        return -1
