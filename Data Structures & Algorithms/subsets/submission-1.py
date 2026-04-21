class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def dfs(curr_sub, start):
            res.append(curr_sub.copy())
            
            if start == n:
                return

            for i in range(start, n):
                curr_sub.append(nums[i])
                dfs(curr_sub, i + 1)
                curr_sub.pop()
        
        dfs([], 0)

        return res