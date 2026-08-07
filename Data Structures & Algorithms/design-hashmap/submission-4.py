class MyHashMap:

    def __init__(self):
        self.keys = [-1] * 1000001
        self.values = [-1] * 1000001

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            self.values[key] = value
        else:
            self.keys[key] = key
            self.values[key] = value

    def get(self, key: int) -> int:
        if key in self.keys:
            return self.values[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.keys:
            self.keys[key] = None
            self.values[key] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)