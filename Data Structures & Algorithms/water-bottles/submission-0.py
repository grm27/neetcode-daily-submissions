class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        empty_bottles = 0
        res = 0

        while numBottles or empty_bottles > numExchange:
            res += numBottles
            empty_bottles += numBottles
            numBottles = empty_bottles // numExchange
            empty_bottles -= numBottles * numExchange

        return res
