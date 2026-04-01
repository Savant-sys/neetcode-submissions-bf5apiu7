class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.arr = [[] for _ in range(1000)]

    def hash(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        index = self.hash(key)
        if key not in self.arr[index]:
            self.arr[index].append(key)

    def remove(self, key: int) -> None:
        index = self.hash(key)
        if key in self.arr[index]:
            self.arr[index].remove(key)

    def contains(self, key: int) -> bool:
        index = self.hash(key)
        return key in self.arr[index]
            


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)