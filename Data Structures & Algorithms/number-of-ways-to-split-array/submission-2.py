class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        left, total = nums[0], sum(nums)
        res = 0

        for i in range(1, len(nums)):
            res += left >= total - left
            left += nums[i]

        return res
