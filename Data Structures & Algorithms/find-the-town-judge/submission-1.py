class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted_count = [0] * n
        trusting_count = [0] * n

        for a, b in trust:
            trusting_count[a - 1] += 1
            trusted_count[b  - 1] += 1
        
        for i in range(n):
            if trusted_count[i] == n - 1 and trusting_count[i] == 0:
                return i + 1
        
        return -1