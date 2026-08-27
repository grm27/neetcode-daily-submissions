class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        present = [False] * (n * n)
        res = []

        for i in range(n):
            for j in range(n):
                index = grid[i][j] - 1
                if present[index]:
                    res.append(index + 1)
                present[index] = True

        for i, p in enumerate(present):
            if not p:
                res.append(i + 1)
                break

        return res
