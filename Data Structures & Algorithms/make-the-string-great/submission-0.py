class Solution:
    def makeGood(self, s: str) -> str:
        offset = abs(ord("a") - ord("A"))
        res = []

        for c in s:
            char_idx = ord(c)
            if res and abs(ord(res[-1]) - char_idx) == offset:
                res.pop()
            else:
                res.append(c)

        return "".join(res)
