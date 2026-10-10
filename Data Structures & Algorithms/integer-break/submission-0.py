class Solution:
    def integerBreak(self, n: int) -> int:
        cache = {}

        def dfs(target):
            if target in cache:
                return cache[target]

            if target <= 2:
                return 1

            cache[target] = max(
                max(i * dfs(target - i), i * (target - i)) for i in range(1, target)
            )
            return cache[target]

        return dfs(n)
