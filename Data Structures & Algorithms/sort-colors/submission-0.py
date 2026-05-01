class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pivot_index = 0

        for i in range(n):
            if nums[i] < 1:
                nums[pivot_index], nums[i] = nums[i], nums[pivot_index]
                pivot_index += 1
        
        for i in range(pivot_index, n):
            if nums[i] < 2:
                nums[pivot_index], nums[i] = nums[i], nums[pivot_index]
                pivot_index += 1