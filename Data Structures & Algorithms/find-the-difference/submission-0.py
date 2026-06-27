class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        n = len(s)
        res = 0

        for i in range(n):
            res ^= ord(s[i]) ^ ord(t[i])

        return chr(res ^ ord(t[n]))
