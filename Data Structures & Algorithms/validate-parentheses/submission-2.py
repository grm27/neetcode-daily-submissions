class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            elif not stack:
                return False
            else:
                opening = stack.pop()
                if (
                    c == "}"
                    and opening != "{"
                    or c == "]"
                    and opening != "["
                    or c == ")"
                    and opening != "("
                ):
                    return False

        return len(stack) == 0
