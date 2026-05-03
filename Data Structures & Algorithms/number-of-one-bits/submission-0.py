class Solution:
    def hammingWeight(self, n: int) -> int:
        hamming_w = 0

        while n > 0:
            hamming_w += n & 1
            n >>= 1
        
        return hamming_w