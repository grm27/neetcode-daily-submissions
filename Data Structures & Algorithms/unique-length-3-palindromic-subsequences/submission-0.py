class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set()
        left = set()
        right = collections.Counter(s)

        for m in range(len(s)):
            right[s[m]] -= 1
            if right[s[m]] == 0:
                del right[s[m]]

            for i in range(26):
                c = chr(i + ord("a"))
                if c in left and c in right:
                    res.add(c + s[m] + c)

            left.add(s[m])

        return len(res)
