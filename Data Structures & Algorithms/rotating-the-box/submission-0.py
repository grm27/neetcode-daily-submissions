class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])

        for row in boxGrid:
            r = n - 1
            for l in range(n - 1, -1, -1):
                if row[l] == "#":
                    row[r], row[l] = row[l], row[r]
                    r -= 1
                if row[l] == "*":
                    r = l - 1

        return [[boxGrid[i][j] for i in range(m - 1, -1, -1)] for j in range(n)]
