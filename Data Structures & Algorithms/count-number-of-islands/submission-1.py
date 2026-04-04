class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != "1":
                return
            
            grid[i][j] = "2"
            for dx, dy in dir:
                dfs(i + dx, j + dy)

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                    dfs(i, j)
        
        return res
            
