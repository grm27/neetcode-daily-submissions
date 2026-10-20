class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        res = 0

        for i in range(1, n):
            nums[i] += nums[i - 1]
            res += nums[i - 1] >= total - nums[i - 1]

        return res
