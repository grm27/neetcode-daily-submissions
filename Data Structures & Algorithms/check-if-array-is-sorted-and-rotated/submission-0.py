class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)

        smallest = 0
        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                smallest = i
                break
        
        for i in range(smallest, smallest + n - 1):
            if nums[i % n] > nums[(i + 1) % n]:
                return False
        
        return True