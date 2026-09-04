class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        perimeter = sum(matchsticks)
        n = len(matchsticks)

        if perimeter % 4 != 0:
            return False

        edge_length = perimeter // 4
        used = [False] * n

        def backtrack(i, edges, target):
            if target == 0:
                return backtrack(0, edges - 1, edge_length)

            if edges == 0:
                return True

            if target < 0 or i >= n:
                return False

            for j in range(i, n):
                if used[j]:
                    continue

                used[j] = True
                if backtrack(j + 1, edges, target - matchsticks[j]):
                    return True
                used[j] = False

            return False

        return backtrack(0, 4, edge_length)
