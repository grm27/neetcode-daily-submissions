class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1] + [0] * (max(0, n - 3 + 1))

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        
        return dp[n]