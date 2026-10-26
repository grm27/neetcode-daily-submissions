class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        stack = []

        for c in s:
            if c != " ":
                stack.append(c)
            else:
                while stack:
                    res.append(stack.pop())
                res.append(" ")

        while stack:
            res.append(stack.pop())

        return "".join(res)
