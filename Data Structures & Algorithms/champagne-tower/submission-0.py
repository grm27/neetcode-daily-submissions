class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        row = [poured]

        for r in range(query_row):
            next_row = [0] * (r + 2)

            for g in range(r + 1):
                excess = max(0, row[g] - 1) / 2
                next_row[g] += excess
                next_row[g + 1] += excess

            row = next_row

        return min(1, row[query_glass])
