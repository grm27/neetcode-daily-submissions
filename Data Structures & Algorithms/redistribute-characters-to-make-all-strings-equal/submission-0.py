class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        concat = "".join(words)
        count = Counter(concat)

        for c in count.values():
            if c % len(words) != 0:
                return False

        return True
