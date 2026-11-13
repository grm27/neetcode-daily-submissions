class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        strings_per_char = 2 ** (n - 1)
        if k > 3 * strings_per_char:
            return ""

        chars = ["a", "b", "c"]
        first_char = (k - 1) // strings_per_char
        k -= first_char * strings_per_char

        res = None
        count = 0

        def backtrack(curr_s):
            nonlocal res, count
            if len(curr_s) == n:
                count += 1
                if count == k:
                    res = curr_s
                return

            if res:
                return

            for c in chars:
                if c != curr_s[-1]:
                    backtrack(curr_s + c)

        backtrack(chars[first_char])
        return res
