class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        tmp = [0] * m

        for _ in range(k):
            for i in range(m - 1):
                tmp[i + 1] = grid[i][n - 1]
            tmp[0] = grid[m - 1][n - 1]

            print(tmp)

            for i in range(m):
                for j in range(n - 1, 0, -1):
                    grid[i][j] = grid[i][j - 1]

            for i in range(m):
                grid[i][0] = tmp[i]

        return grid
