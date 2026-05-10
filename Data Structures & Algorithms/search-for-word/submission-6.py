class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        visited = [[False] * n for _ in range(m)]

        def dfs(i, row, col):
            if i == len(word):
                return True

            if row < 0 or col < 0 or row >= m or col >= n or visited[row][col] or board[row][col] != word[i]:
                return False
            
            visited[row][col] = True
            for dr, dc in dirs:
                next_row, next_col = row + dr, col + dc
                if dfs(i + 1, next_row, next_col):
                    return True
            visited[row][col] = False

            return False
        
        for i in range(m):
            for j in range(n):
                if dfs(0, i, j):
                    return True
        
        return False
        

