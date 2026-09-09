class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def can_eat(k):
            total_time = 0
            for p in piles:
                total_time += math.ceil(p / k)
                if total_time > h:
                    return False
            return True

        l, r = 1, max(piles)

        while l < r:
            mid = (l + r) // 2

            if can_eat(mid):
                r = mid
            else:
                l = mid + 1

        return l
