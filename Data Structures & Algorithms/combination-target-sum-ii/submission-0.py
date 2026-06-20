class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        res = []

        def backtrack(i, curr_comb, curr_sum):
            if i > n or curr_sum > target:
                return

            if curr_sum == target:
                res.append(curr_comb.copy())
                return

            j = i
            while j < n:
                curr_comb.append(candidates[j])
                backtrack(j + 1, curr_comb, curr_sum + candidates[j])
                del curr_comb[-1]
                while j + 1 < n and candidates[j] == candidates[j + 1]:
                    j += 1
                j += 1

        backtrack(0, [], 0)
        return res
