class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        cache = {}

        def dfs(i, curr_sum):
            state = (i, curr_sum)
            if state in cache:
                return cache[state]

            if i == n:
                return 1 if curr_sum == target else 0
            
            cache[state] = dfs(i + 1, curr_sum + nums[i]) + dfs(i + 1, curr_sum - nums[i])
            return cache[state]

        return dfs(0, 0)