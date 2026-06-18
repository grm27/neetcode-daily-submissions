class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(i, j, dist):
            if i < 0 or j < 0 or i == m or j == n or grid[i][j] < dist:
                return
            
            grid[i][j] = dist
            for di, dj in dirs:
                dfs(i + di, j + dj, dist + 1)

            

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    dfs(i, j, 0)