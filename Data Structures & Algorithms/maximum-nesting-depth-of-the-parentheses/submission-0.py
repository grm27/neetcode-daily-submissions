class Solution:
    def maxDepth(self, s: str) -> int:
        res = depth = 0

        for c in s:
            depth -= c == ")"
            depth += c == "("
            res = max(res, depth)

        return res
