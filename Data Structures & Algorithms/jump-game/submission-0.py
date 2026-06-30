class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        farest = 0

        for i in range(n):
            if i > farest:
                return False
            farest = max(farest, i + nums[i])
            if farest >= n - 1:
                return True
        
        return False

    
        