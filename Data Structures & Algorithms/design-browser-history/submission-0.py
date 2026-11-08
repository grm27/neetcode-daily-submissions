class BrowserHistory:
    def __init__(self, homepage: str):
        self.visited = [homepage]
        self.fwd = []

    def visit(self, url: str) -> None:
        self.visited.append(url)
        self.fwd.clear()

    def back(self, steps: int) -> str:
        for _ in range(min(steps, len(self.visited) - 1)):
            self.fwd.append(self.visited.pop())
        return self.visited[-1]

    def forward(self, steps: int) -> str:
        for _ in range(min(steps, len(self.fwd))):
            self.visited.append(self.fwd.pop())
        return self.visited[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
