class Solution:
    def __init__(self, w: List[int]):
        self.distribution = []
        for i, weight in enumerate(w):
            self.distribution += [i] * weight

    def pickIndex(self) -> int:
        return self.distribution[random.randrange(len(self.distribution))]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
