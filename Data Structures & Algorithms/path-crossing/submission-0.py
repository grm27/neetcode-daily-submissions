class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set([(0, 0)])
        x = y = 0

        for dir in path:
            if dir == "N":
                y += 1
            elif dir == "S":
                y -= 1
            elif dir == "W":
                x += 1
            else:
                x -= 1

            if (x, y) in visited:
                return True

            visited.add((x, y))

        return False
