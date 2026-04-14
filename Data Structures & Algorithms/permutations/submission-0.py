class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def backtrack(curr_permutation, used):
            if len(curr_permutation) == n:
                res.append(curr_permutation.copy())
                return
            
            for num in nums:
                if num in used: 
                    continue
                curr_permutation.append(num)
                used.add(num)
                backtrack(curr_permutation, used)
                used.remove(num)
                del curr_permutation[-1]
            
        backtrack([], set())

        return res