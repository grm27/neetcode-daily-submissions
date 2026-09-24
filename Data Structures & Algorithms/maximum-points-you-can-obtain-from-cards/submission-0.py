class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        score = sum(cardPoints[i] for i in range(k))
        res = score

        for i in range(k):
            score += cardPoints[n - 1 - i] - cardPoints[k - 1 - i]
            res = max(res, score)

        return res
