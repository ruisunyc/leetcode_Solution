class LRUCache:

    def __init__(self, capacity: int):
        self.d = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.d:return -1
        self.d.move_to_end(key,last = True)
        return self.d[key]

    def put(self, key: int, value: int) -> None:
        if len(self.d)>=self.capacity and key not in self.d:
            self.d.popitem(last=False)
        self.d[key] = value
        self.d.move_to_end(key,last=True)
                




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)