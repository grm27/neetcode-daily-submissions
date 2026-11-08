class Solution:
    def smallestNumber(self, pattern: str) -> str:
        pattern = "I" + pattern
        n = len(pattern)
        used = [False] * 9

        def backtrack(prev, i, num):
            if i == n + 1:
                return num

            num_range = range(prev + 1, 10) if pattern[i - 1] == "I" else range(1, prev)

            for d in num_range:
                if not used[d - 1]:
                    used[d - 1] = True
                    res = backtrack(d, i + 1, num + str(d))
                    if res:
                        return res
                    used[d - 1] = False

            return None

        return backtrack(0, 1, "")
