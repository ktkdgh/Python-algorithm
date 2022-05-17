# 정답
import collections

class MyCircularDeque:

    def __init__(self, k: int):
        self.q = collections.deque()
        self.maxlen = k

    def insertFront(self, value: int) -> bool:
        self.q.appendleft(value)
        if len(self.q) > self.maxlen:
            self.q.popleft()
            return False
        return True

    def insertLast(self, value: int) -> bool:
        self.q.append(value)
        if len(self.q) > self.maxlen:
            self.q.pop()
            return False
        return True

    def deleteFront(self) -> bool:
        if len(self.q):
            self.q.popleft()
            return True
        return False

    def deleteLast(self) -> bool:
        if len(self.q):
            self.q.pop()
            return True
        return False

    def getFront(self) -> int:
        if len(self.q):
            return self.q[0]
        return -1
    def getRear(self) -> int:
        if len(self.q):
            return self.q[-1]
        return -1

    def isEmpty(self) -> bool:
        return len(self.q) == 0

    def isFull(self) -> bool:
        return len(self.q) == self.maxlen


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()