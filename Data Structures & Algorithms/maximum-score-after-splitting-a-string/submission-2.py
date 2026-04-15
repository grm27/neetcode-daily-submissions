class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
    
        prefix_sum = [ord(c) - ord("0") for c in s]
        for i in range(1, n):
            prefix_sum[i] += prefix_sum[i - 1]  
                
        res = 0
        for i in range(n - 1):
            res = max(res, prefix_sum[n - 1] + i + 1 - 2 * prefix_sum[i])
           
        return res