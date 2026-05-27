class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(r, c):
            if r < 0 or c < 0 or r == m or c == n or visited[r][c] or not grid[r][c]:
                return 0
            
            visited[r][c] = True
            
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
        
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))
        
        return res