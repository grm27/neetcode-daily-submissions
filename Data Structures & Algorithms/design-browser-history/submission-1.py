class Node:
    def __init__(self, val):
        self.prev = None
        self.next = None
        self.val = val


class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = Node(homepage)

    def visit(self, url: str) -> None:
        new_node = Node(url)
        new_node.prev = self.history
        self.history.next = new_node
        self.history = new_node

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if not self.history.prev:
                break
            self.history = self.history.prev

        return self.history.val

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if not self.history.next:
                break
            self.history = self.history.next
        return self.history.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
