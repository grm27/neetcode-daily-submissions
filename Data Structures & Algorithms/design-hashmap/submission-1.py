class MyHashMap:

    def __init__(self):
        self.size = 9997
        self.values = [None] * self.size
        

    def put(self, key: int, value: int) -> None:
        self.values[key % self.size] = value

    def get(self, key: int) -> int:
        val = self.values[key % self.size]
        return val if val is not None else -1 

    def remove(self, key: int) -> None:
        self.values[key % self.size] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)