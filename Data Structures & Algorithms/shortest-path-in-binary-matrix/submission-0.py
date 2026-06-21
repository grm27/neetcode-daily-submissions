class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, 1), (1, -1), (-1, -1), (1, 1)]
        min_heap = [(1, 0, 0)]
        min_dist = [[float("inf")] * n for _ in range(n)]

        while min_heap:
            dist, x, y = heapq.heappop(min_heap)

            if grid[x][y] == 1:
                continue

            if x == n - 1 and y == n - 1:
                return dist

            grid[x][y] = 1

            for dx, dy in dirs:
                nei_x, nei_y = x + dx, y + dy
                if (
                    nei_x >= 0
                    and nei_y >= 0
                    and nei_x < n
                    and nei_y < n
                    and dist + 1 < min_dist[nei_x][nei_y]
                ):
                    min_dist[nei_x][nei_y] = dist + 1
                    heapq.heappush(min_heap, (dist + 1, nei_x, nei_y))

        return -1
