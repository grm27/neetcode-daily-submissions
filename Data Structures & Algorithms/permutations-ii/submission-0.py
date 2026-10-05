class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        used = set()

        def backtrack(curr_res):
            if len(curr_res) == n:
                res.append(curr_res.copy())
                return

            i = 0
            while i < n:
                if i not in used:
                    used.add(i)
                    curr_res.append(nums[i])
                    backtrack(curr_res)
                    used.remove(i)
                    curr_res.pop()
                    while i < n - 1 and nums[i] == nums[i + 1]:
                        i += 1

                i += 1

        backtrack([])
        return res
