class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row_count = [0] * m
        column_count = [0] * n

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    row_count[i] += 1
                    column_count[j] += 1

        res = 0
        for i in range(m):
            if row_count[i] > 1:
                res += row_count[i]
                grid[i] = [0] * n

        for j in range(n):
            if column_count[j] > 1:
                for i in range(m):
                    res += grid[i][j]

        return res
