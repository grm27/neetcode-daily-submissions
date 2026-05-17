class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)
        
        curr_sum = nums[0]
        res = curr_sum

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                curr_sum += nums[i]
            else:
                curr_sum = nums[i]
            res = max(res, curr_sum)
        
        return res