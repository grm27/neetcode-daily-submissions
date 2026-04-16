class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        consecutive_ones = 0

        for n in nums:
            consecutive_ones = consecutive_ones * n + n
            res = max(res, consecutive_ones)
        
        return res