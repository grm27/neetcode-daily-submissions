class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []

        def backtrack(curr_subset, i):
            res.append(curr_subset.copy())

            j = i
            while j < n:
                curr_subset.append(nums[j])
                backtrack(curr_subset, j + 1)
                del curr_subset[-1]

                while j < n - 1 and nums[j] == nums[j + 1]:
                    j += 1
                j += 1
        
        backtrack([], 0)
        
        return res