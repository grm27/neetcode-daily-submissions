class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(start, curr_combination):
            if len(curr_combination) == k:
                res.append(curr_combination.copy())
                return
            
            for i in range(start, n + 1):
                curr_combination.append(i)
                backtrack(i + 1, curr_combination)
                del curr_combination[-1]
        
        backtrack(1, [])

        return res
