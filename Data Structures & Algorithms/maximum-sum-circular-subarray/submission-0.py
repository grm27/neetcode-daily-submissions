class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        curr_min = curr_max = nums[0]
        total = global_min = global_max = nums[0]

        for n in nums[1:]:
            curr_min = min(n, curr_min + n)
            global_min = min(global_min, curr_min)
            curr_max = max(n, curr_max + n)
            global_max = max(global_max, curr_max)
            total += n

        return max(total - global_min, global_max) if global_max > 0 else global_max
