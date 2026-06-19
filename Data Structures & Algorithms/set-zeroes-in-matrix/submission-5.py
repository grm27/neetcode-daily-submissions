class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        first_row = first_column = False

        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    matrix[0][j] = matrix[i][0] = 0
                    first_row |= i == 0
                    first_column |= j == 0

        for i in range(1, m):
            for j in range(1, n):
                if not matrix[0][j] or not matrix[i][0]:
                    matrix[i][j] = 0

        if first_row:
            for j in range(n):
                matrix[0][j] = 0
        if first_column:
            for i in range(m):
                matrix[i][0] = 0
