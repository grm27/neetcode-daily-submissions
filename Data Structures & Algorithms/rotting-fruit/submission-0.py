class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh_oranges = 0
        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                else:
                    fresh_oranges += grid[i][j]

        minutes = 0
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while queue and fresh_oranges:

            for _ in range(len(queue)):
                i, j = queue.popleft()

                for di, dj in dirs:
                    next_i, next_j = i + di, j + dj
                    if (
                        next_i >= 0
                        and next_j >= 0
                        and next_i < m
                        and next_j < n
                        and grid[next_i][next_j] == 1
                    ):
                        queue.append((next_i, next_j))
                        grid[next_i][next_j] = 2
                        fresh_oranges -= 1

            minutes += 1

        return minutes if not fresh_oranges else -1
