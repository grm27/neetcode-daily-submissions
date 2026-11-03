class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        empty = 0
        res = 0

        while numBottles or empty > numExchange:
            res += numBottles
            empty += numBottles
            numBottles = empty // numExchange
            empty -= numBottles * numExchange

        return res
