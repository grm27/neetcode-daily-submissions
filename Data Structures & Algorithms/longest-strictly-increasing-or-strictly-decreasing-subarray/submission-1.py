class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res = strictly_increasing = strictly_decreasing = 1

        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                strictly_increasing = 0

            strictly_increasing += 1
            res = max(res, strictly_increasing)

        for i in range(1, len(nums)):
            if nums[i - 1] <= nums[i]:
                strictly_decreasing = 0

            strictly_decreasing += 1
            res = max(res, strictly_decreasing)

        return res
