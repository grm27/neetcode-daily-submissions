class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, 1), (1, -1), (-1, -1), (1, 1)]
        queue = deque()
        queue.append((0, 0, 1))

        if grid[0][0] == 1:
            return -1

        grid[0][0] = 1

        while queue:
            x, y, dist = queue.popleft()

            if x == n - 1 and y == n - 1:
                return dist

            for dx, dy in dirs:
                nei_x, nei_y = x + dx, y + dy
                if (
                    nei_x >= 0
                    and nei_y >= 0
                    and nei_x < n
                    and nei_y < n
                    and grid[nei_x][nei_y] == 0
                ):
                    grid[nei_x][nei_y] = 1
                    queue.append((nei_x, nei_y, dist + 1))

        return -1
