# 정답
class MyHashMap:

    def __init__(self):
        self.q = {}

    def put(self, key: int, value: int) -> None:
        self.q[key] = value

    def get(self, key: int) -> int:
        if key in self.q.keys():
            return self.q[key]
        else:
            return -1
    def remove(self, key: int) -> None:
        if key in self.q.keys():
            del self.q[key]
            return
        else:
            return

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
