class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        columns = [False] * n
        diagonals = [False] * (2 * n - 1)
        counter_diagonals = [False] * (2 * n - 1)

        def backtrack(curr_sol, row):
            if len(curr_sol) == n:
                res.append(curr_sol.copy())
                return

            for i in range(n):
                if (
                    not columns[i]
                    and not diagonals[(i - row) + (n - 1)]
                    and not counter_diagonals[i + row]
                ):
                    columns[i] = diagonals[(i - row) + (n - 1)] = counter_diagonals[i + row] = True
                    queen = ["."] * n
                    queen[i] = "Q"
                    curr_sol.append("".join(queen))
                    backtrack(curr_sol, row + 1)
                    curr_sol.pop()
                    columns[i] = diagonals[(i - row) + (n - 1)] = counter_diagonals[i + row] = False

        backtrack([], 0)

        return res
