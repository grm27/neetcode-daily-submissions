class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        last_occurence = [-1] * 26

        for i in range(n):
            last_occurence[ord(s[i]) - ord("a")] = i

        start, end = 0, 0
        res = []
        for i in range(n + 1):
            if i > end:
                res.append(end - start + 1)
                start = i
            if i < n:
                end = max(end, last_occurence[ord(s[i]) - ord("a")])

        return res
