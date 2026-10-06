class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        queue = deque()

        for i in [0, m - 1]:
            for j in range(n):
                if board[i][j] == "O":
                    queue.append((i, j))

        for j in [0, n - 1]:
            for i in range(1, m - 1):
                if board[i][j] == "O":
                    queue.append((i, j))

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            i, j = queue.popleft()

            board[i][j] = "T"
            for di, dj in dirs:
                next_i, next_j = i + di, j + dj
                if (
                    next_i >= 0
                    and next_i < m
                    and next_j >= 0
                    and next_j < n
                    and board[next_i][next_j] == "O"
                ):
                    queue.append((next_i, next_j))

        for i in range(m):
            for j in range(n):
                if board[i][j] == "T":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"
