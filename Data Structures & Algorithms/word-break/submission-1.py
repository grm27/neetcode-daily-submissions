class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {}
        word_set = set(wordDict)

        def dfs(i):
            if i in cache:
                return cache[i]

            if i == len(s):
                return True

            for j in range(i, len(s)):
                if s[i : j + 1] in word_set and dfs(j + 1):
                    cache[i] = True
                    return cache[i]

            cache[i] = False
            return cache[i]

        return dfs(0)
