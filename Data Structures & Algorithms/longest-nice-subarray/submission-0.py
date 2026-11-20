class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        res = 1
        l = 0
        curr = 0

        for r in range(len(nums)):
            while curr & nums[r] != 0:
                curr ^= nums[l]
                l += 1
            curr |= nums[r]
            res = max(res, r - l + 1)

        return res
