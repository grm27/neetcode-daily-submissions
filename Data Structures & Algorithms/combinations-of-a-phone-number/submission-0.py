class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_dict = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        res = []

        if not digits:
            return res

        def backtrack(curr_s):
            if len(curr_s) == len(digits):
                res.append("".join(curr_s))
                return

            for c in digit_dict[digits[len(curr_s)]]:
                curr_s.append(c)
                backtrack(curr_s)
                curr_s.pop()

        backtrack([])
        return res
