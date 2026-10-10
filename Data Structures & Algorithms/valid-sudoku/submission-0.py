class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            visited = [False] * 9
            for j in range(9):
                if board[i][j] != ".":
                    num = ord(board[i][j]) - ord("1")
                    if visited[num]:
                        return False
                    visited[num] = True

        for j in range(9):
            visited = [False] * 9
            for i in range(9):
                if board[i][j] != ".":
                    num = ord(board[i][j]) - ord("1")
                    if visited[num]:
                        return False
                    visited[num] = True

        for di in [0, 3, 6]:
            for dj in [0, 3, 6]:
                visited = [False] * 9
                for i in range(3):
                    for j in range(3):
                        char = board[i + di][j + dj]
                        if char != ".":
                            num = ord(char) - ord("1")
                            if visited[num]:
                                return False
                            visited[num] = True

        return True
