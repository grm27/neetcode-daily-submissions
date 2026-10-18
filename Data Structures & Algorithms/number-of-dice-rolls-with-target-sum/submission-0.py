class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        cache = {}

        def dfs(n, target):
            state = (n, target)
            if n == 0:
                return int(target == 0)

            if state in cache:
                return cache[state]

            cache[state] = sum(dfs(n - 1, target - i) for i in range(1, min(k, target) + 1))
            return cache[state] % 1000000007

        return dfs(n, target)
