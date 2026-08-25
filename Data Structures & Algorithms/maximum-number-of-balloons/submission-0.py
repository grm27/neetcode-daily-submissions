class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        char_count = Counter(text)

        return min(
            char_count["b"],
            char_count["a"],
            char_count["l"] // 2,
            char_count["o"] // 2,
            char_count["n"],
        )
