class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
    
        for i in range(1, n):
            first_digit = ord(s[i]) - ord("0")
            second_digit = ord(s[i - 1]) - ord("0")

            if first_digit > 0:
                dp[i + 1] += dp[i]
            
            number = second_digit * 10 + first_digit
            if number >= 10 and number <= 26:
                dp[i + 1] += dp[i - 1]
            
            if dp[i + 1] == 0:
                return 0
       
        return dp[n]

