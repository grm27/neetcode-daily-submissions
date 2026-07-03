class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        min_val = self.stack[-1][1] if self.stack else float("inf")
        self.stack.append((val, min(min_val, val)))

    def pop(self) -> None:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
