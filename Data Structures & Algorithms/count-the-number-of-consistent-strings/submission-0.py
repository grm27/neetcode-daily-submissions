class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set([ord(c) for c in allowed])
        res = 0

        for word in words:
            consistent = True
            for c in word:
                if ord(c) not in allowed:
                    consistent = False
                    break
            res += consistent

        return res
