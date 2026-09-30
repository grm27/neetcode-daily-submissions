class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        res = l = 0

        max_f = 0
        for r in range(len(s)):
            counter[s[r]] += 1
            max_f = max(max_f, counter[s[r]])
            while r - l + 1 - max_f > k:
                counter[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res
