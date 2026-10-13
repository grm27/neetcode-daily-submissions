class FreqStack:
    def __init__(self):
        self.counter = defaultdict(int)
        self.values = []

    def push(self, val: int) -> None:
        count = self.counter[val] + 1
        if count > len(self.values):
            self.values.append([])
        self.values[count - 1].append(val)
        self.counter[val] = count

    def pop(self) -> int:
        el = self.values[-1].pop()
        self.counter[el] -= 1
        if not self.values[-1]:
            self.values.pop()
        return el


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
