class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            root = 1
            while root**2 <= i:
                dp[i] = min(dp[i], dp[i - root**2] + 1)
                root += 1

        return dp[n]
