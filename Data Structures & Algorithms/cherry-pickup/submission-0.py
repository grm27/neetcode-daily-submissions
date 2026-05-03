class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        cache = {}

        def dfs(r1, c1, r2):
            state = (r1, c1, r2)
            if state in cache:
                return cache[state]

            c2 = r1 + c1 - r2
            if (
                r1 >= n
                or c1 >= n
                or r2 >= n
                or c2 >= n
                or grid[r1][c1] == -1
                or grid[r2][c2] == -1
            ):
                return -float("inf")

            cherries = grid[r1][c1]

            if r1 == n - 1 and c1 == n - 1:
                return cherries

            if (r2, c2) != (r1, c1):
                cherries += grid[r2][c2]

            cache[state] = cherries + max(
                dfs(r1 + 1, c1, r2),
                dfs(r1, c1 + 1, r2),
                dfs(r1 + 1, c1, r2 + 1),
                dfs(r1, c1 + 1, r2 + 1),
            )
            return cache[state]

        return max(0, dfs(0, 0, 0))
