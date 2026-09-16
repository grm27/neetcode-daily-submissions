class Solution:
    def __init__(self, w: List[int]):
        self.distribution = w
        for i in range(1, len(w)):
            self.distribution[i] += self.distribution[i - 1]

    def pickIndex(self) -> int:
        rand = random.randint(1, self.distribution[-1])
        left, right = 0, len(self.distribution) - 1

        while left < right:
            mid = (left + right) // 2
            if self.distribution[mid] < rand:
                left = mid + 1
            else:
                right = mid

        return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
