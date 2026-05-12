class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_chars = [0] * 26
        magazine_chars = [0] * 26

        for c in ransomNote:
            ransom_chars[ord(c) - ord("a")] += 1
        
        for c in magazine:
            magazine_chars[ord(c) - ord("a")] += 1
        
        for i in range(26):
            if magazine_chars[i] < ransom_chars[i]:
                return False
        
        return True
