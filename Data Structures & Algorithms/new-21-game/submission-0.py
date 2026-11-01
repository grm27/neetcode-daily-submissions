class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        window_sum = 0
        dp = {}

        for i in range(k, k + maxPts):
            dp[i] = i <= n
            window_sum += i <= n

        for i in range(k - 1, -1, -1):
            dp[i] = window_sum / maxPts
            window_sum += dp[i] - dp[i + maxPts]
        
        return dp[0]
