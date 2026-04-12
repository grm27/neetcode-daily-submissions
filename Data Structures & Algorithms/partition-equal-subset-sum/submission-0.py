class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        
        if total % 2 != 0:
            return False
        
        half = total // 2
        cache = {}
        def dfs(i, curr_sum):
            if (i, curr_sum) in cache:
                return cache[(i, curr_sum)]
            
            if curr_sum == half:
                return True

            if i >= n or curr_sum > half:
                return False
            
            cache[(i, curr_sum)] = dfs(i + 1, curr_sum) or dfs(i + 1, curr_sum + nums[i])
            return cache[(i, curr_sum)]
        return dfs(0, 0)