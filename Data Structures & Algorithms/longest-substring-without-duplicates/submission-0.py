class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = l = 0
        window_chars = set()

        for r in range(len(s)):
            while l < r and s[r] in window_chars:
                window_chars.remove(s[l])
                l += 1
            window_chars.add(s[r])
            res = max(res, r - l + 1)

        return res
