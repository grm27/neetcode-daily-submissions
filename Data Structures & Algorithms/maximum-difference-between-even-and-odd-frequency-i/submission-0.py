class Solution:
    def maxDifference(self, s: str) -> int:
        count = [0] * 26

        for c in s:
            count[ord(c) - ord("a")] += 1

        max_odd, min_even = 0, float("inf")

        for c in count:
            if c % 2 == 0 and c != 0:
                min_even = min(min_even, c)
            else:
                max_odd = max(max_odd, c)

        return max_odd - min_even
