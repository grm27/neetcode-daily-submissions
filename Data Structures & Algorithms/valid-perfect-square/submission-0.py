class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, num // 2

        while l < r:
            m = (l + r) // 2
            if m**2 >= num:
                r = m
            else:
                l = m + 1

        return l**2 == num
