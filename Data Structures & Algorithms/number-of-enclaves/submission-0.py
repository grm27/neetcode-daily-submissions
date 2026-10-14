class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def dfs(i, j):
            if grid[i][j] != 1:
                return

            grid[i][j] = 0

            for di, dj in dirs:
                next_i, next_j = i + di, j + dj
                if next_i >= 0 and next_i < m and next_j >= 0 and next_j < n:
                    dfs(next_i, next_j)

        for i in [0, m - 1]:
            for j in range(n):
                dfs(i, j)

        for j in [0, n - 1]:
            for i in range(m):
                dfs(i, j)

        res = 0
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                res += grid[i][j]

        return res
