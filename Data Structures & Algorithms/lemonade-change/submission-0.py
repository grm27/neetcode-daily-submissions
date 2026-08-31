class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = [0] * 2

        for bill in bills:
            change[0] += (bill == 5) - (bill != 5)
            change[1] += bill == 10

            if bill == 20:
                change[0] -= 2 * (change[1] < 1)
                change[1] -= change[1] > 0
                
            if change[0] < 0 or change[1] < 0:
                return False

        return True
