class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n

        while l < r:
            m = (l + r) // 2

            sum = (m * (m + 1)) // 2

            if sum < n:
                l = m + 1
            else:
                r = m

        return l - 1 if (l * (l + 1)) // 2 > n else l
