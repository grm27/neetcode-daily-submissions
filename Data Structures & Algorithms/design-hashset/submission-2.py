class MyHashSet:

    def __init__(self):
        self.size = 9997
        self.set = [False] * self.size

    def add(self, key: int) -> None:
        self.set[key % self.size] = True

    def remove(self, key: int) -> None:
        self.set[key % self.size] = False

    def contains(self, key: int) -> bool:
        return  self.set[key % self.size]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)