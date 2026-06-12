class Solution:
    def reverse(self, x: int) -> int:
        low = 2 ** 31
        high = 2 ** 31 - 1
        negative = x < 0

        res = 0
        x = abs(x)
        while x:
            res = res * 10 + x % 10
            x //= 10
        
        res = -res if negative else res

        if res < -low or res > high:
            return 0

        return res