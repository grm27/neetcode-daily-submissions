class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        dist = 0

        for n in nums:
            dist ^= n

        bit_mask = 1
        while bit_mask & dist == 0:
            bit_mask <<= 1

        p1 = p2 = 0
        for n in nums:
            if bit_mask & n:
                p1 ^= n
            else:
                p2 ^= n

        return [p1, p2]
