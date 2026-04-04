class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(n):
            letter = int(s[i])
            if letter >=1 and letter <= 26:
                dp[i + 1] += dp[i]
            if i >= 1:
                letter = int(s[i - 1: i + 1])
                if letter >=10 and letter <= 26:
                    dp[i + 1] += dp[i-1]
            if dp[i + 1] == 0:
                return 0
        
        return dp[n]

