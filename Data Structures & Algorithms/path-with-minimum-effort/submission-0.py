class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = [(0, 0, 0)]
        cost = [[float("inf")] * n for _ in range(m)]

        while queue:
            c, i, j = heapq.heappop(queue)

            if i == m - 1 and j == n - 1:
                return c

            for di, dj in dirs:
                nei_i, nei_j = i + di, j + dj
                if nei_i < 0 or nei_i == m or nei_j < 0 or nei_j == n:
                    continue
                nei_cost = max(c, abs(heights[i][j] - heights[nei_i][nei_j]))

                if nei_cost < cost[nei_i][nei_j]:
                    cost[nei_i][nei_j] = nei_cost
                    heapq.heappush(queue, (nei_cost, nei_i, nei_j))
