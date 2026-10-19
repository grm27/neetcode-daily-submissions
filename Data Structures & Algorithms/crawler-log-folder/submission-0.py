class Solution:
    def minOperations(self, logs: list[str]) -> int:
        stack_len = 0

        for log in logs:
            if log == "../":
                stack_len = max(0, stack_len - 1)
            elif log != "./":
                stack_len += 1

        return stack_len
