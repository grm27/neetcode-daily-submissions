class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        if n > m:
            return -1
        
        for i in range(m - n + 1):
            match = True

            for j in range(n):
                if haystack[i + j] != needle[j]:
                    match = False
                    break
            
            if match:
                return i
        
        return -1