class RandomizedSet:
    def __init__(self):
        self.values = []
        self.idx = {}

    def insert(self, val: int) -> bool:
        if val in self.idx:
            return False
        self.idx[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.idx:
            return False
        i = self.idx[val]
        last_val = self.values[-1]
        self.values[i] = last_val
        self.idx[last_val] = i
        self.values.pop()
        del self.idx[val]
        return True

    def getRandom(self) -> int:
        i = random.randrange(len(self.values))
        return self.values[i]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
