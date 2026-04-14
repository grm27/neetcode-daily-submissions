class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def backtrack(curr_permutation):
            if len(curr_permutation) == n:
                res.append(curr_permutation.copy())
                return
            
            for i in range(n):
                num = nums[i]
                if num > 10:
                    continue
                curr_permutation.append(num)
                nums[i] = 11
                backtrack(curr_permutation)
                nums[i] = num
                del curr_permutation[-1]
            
        backtrack([])

        return res