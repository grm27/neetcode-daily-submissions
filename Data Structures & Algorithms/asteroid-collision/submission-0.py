class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []

        for asteroid in asteroids:
            if asteroid < 0:
                while res and 0 < res[-1] < -asteroid:
                    res.pop()
                if res and res[-1] > 0:
                    if res[-1] == -asteroid:
                        res.pop()
                    continue

            res.append(asteroid)

        return res
