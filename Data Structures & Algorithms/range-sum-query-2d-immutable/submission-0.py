class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            for j in range(1, n):
                matrix[i][j] += matrix[i][j - 1]

        for j in range(n):
            for i in range(1, m):
                matrix[i][j] += matrix[i - 1][j]

        self.prefix_sum_matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = self.prefix_sum_matrix[row2][col2]
        row1 -= 1
        col1 -= 1

        if row1 >= 0:
            res -= self.prefix_sum_matrix[row1][col2]
        if col1 >= 0:
            res -= self.prefix_sum_matrix[row2][col1]
        if row1 >= 0 and col1 >= 0:
            res += self.prefix_sum_matrix[row1][col1]

        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
