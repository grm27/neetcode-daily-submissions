class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])

        dp = points[0]
        for i in range(1, m):
            left = [0] * n
            left[0] = dp[0]
            for j in range(1, n):
                left[j] = max(left[j - 1] - 1, dp[j])

            right = [0] * n
            right[n - 1] = dp[n - 1]
            for j in range(1, n):
                right[n - 1 - j] = max(right[n - j] - 1, dp[n - 1 - j])

            next_dp = points[i]
            for j in range(n):
                next_dp[j] += max(left[j], right[j])

            dp = next_dp

        return max(dp)
