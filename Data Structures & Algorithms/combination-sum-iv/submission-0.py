class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        cache = {}
        def backtrack(curr_sum):
            if curr_sum in cache:
                return cache[curr_sum]
            if curr_sum > target:
                return 0

            if curr_sum == target:
                return 1
            
            res = 0
            for n in nums:
                res += backtrack(curr_sum + n)
            cache[curr_sum] = res
            return res
        
        return backtrack(0)