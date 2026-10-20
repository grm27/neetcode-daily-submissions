class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = nums.copy()

        for i in range(1, n):
            prefix_sum[i] += prefix_sum[i - 1]

        return sum(prefix_sum[i - 1] >= (prefix_sum[-1] - prefix_sum[i - 1]) for i in range(1, n))
