class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        perimeter = 0
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    perimeter += 4
                    for di, dj in dirs:
                        if i + di >= 0 and i + di < m and j + dj >= 0 and j + dj < n:
                            perimeter -= grid[i + di][j + dj]
        return perimeter