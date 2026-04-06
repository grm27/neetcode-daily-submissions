class Solution:
    def jump(self, nums: List[int]) -> int:
        left, right = 0, 0
        jumps = 0

        while right < len(nums) - 1:
            farest = right
            for i in range(left, right + 1):
                farest = max(farest, nums[i] + i)
            left = right + 1
            right = farest
            jumps += 1
        
        return jumps