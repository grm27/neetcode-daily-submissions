class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False

        cache = {}

        def dfs(i, j):
            state = (i, j)

            if i + j == len(s3):
                return True

            if state in cache:
                return cache[state]

            k = i + j

            if (
                i < len(s1)
                and s1[i] == s3[k]
                and dfs(i + 1, j)
                or j < len(s2)
                and s2[j] == s3[k]
                and dfs(i, j + 1)
            ):
                cache[state] = True
            else:
                cache[state] = False

            return cache[state]

        return dfs(0, 0)
