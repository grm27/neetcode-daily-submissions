class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i, j = 0, 0
        while j < len(t):
            while i < len(s) and t[j] != s[i]:
                i += 1
            if i == len(s):
                break
            i += 1
            j += 1
        
        return len(t) - j