class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        sum_missing = mean * (n + len(rolls)) - sum(rolls)

        if sum_missing > 6 * n or sum_missing < n:
            return []

        res = [sum_missing // n] * n

        remainder = sum_missing % n
        i = 0
        while remainder:
            decrement = min(6 - res[i], remainder)
            remainder -= decrement
            res[i] += decrement
            i += 1
        return res
