class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)

        if n > m:
            return ""

        t_count = Counter(t)

        matching_chars = 0
        window_count = defaultdict(int)
        min_window = float("inf")
        res = [0, 0]

        l = 0
        for r in range(m):
            window_count[s[r]] += 1

            if s[r] in t_count and window_count[s[r]] <= t_count[s[r]]:
                matching_chars += 1

            while l < r and (s[l] not in t_count or window_count[s[l]] > t_count[s[l]]):
                window_count[s[l]] -= 1
                l += 1

            if matching_chars == n and r - l + 1 < min_window:
                res = [l, r + 1]
                min_window = r - l + 1

        return s[res[0] : res[1]]
