class Solution:
    def totalNQueens(self, n: int) -> int:

        used_diagonals = set()
        used_counter_diagonals = set()
        used_columns = set()

        def dfs(row):
            if row == n:
                return 1

            solutions = 0

            for col in range(n):
                diagonal = row - col
                counter_diagonal = row + col
                if (
                    col not in used_columns
                    and diagonal not in used_diagonals
                    and counter_diagonal not in used_counter_diagonals
                ):
                    used_diagonals.add(diagonal)
                    used_counter_diagonals.add(counter_diagonal)
                    used_columns.add(col)
                    solutions += dfs(row + 1)
                    used_diagonals.remove(diagonal)
                    used_counter_diagonals.remove(counter_diagonal)
                    used_columns.remove(col)

            return solutions

        return dfs(0)
