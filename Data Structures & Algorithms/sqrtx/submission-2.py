class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x

        while l < r:
            mid = (l + r) // 2
            square = mid * mid
            if square < x:
                l = mid + 1
            else:
                r = mid

        return l if l * l == x else l - 1
