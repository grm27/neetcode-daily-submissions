class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        cache = {}

        def dfs(i, buy):
            state = (i, buy)
            if i >= n:
                return 0

            if state in cache:
                return cache[state]

            if buy:
                cache[state] = max(-prices[i] + dfs(i + 1, not buy), dfs(i + 1, buy))
            else:
                cache[state] = max(prices[i] + dfs(i + 2, not buy), dfs(i + 1, buy))

            return cache[state]

        return dfs(0, True)
