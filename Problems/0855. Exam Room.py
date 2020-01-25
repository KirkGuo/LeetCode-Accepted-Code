class ExamRoom:

    def __init__(self, N: int):
        self.cap = N
        self.data = []

    def seat(self) -> int:
        if not self.data:
            pos = 0
        else:
            dist = self.data[0]
            pos = 0
            for idx, each in enumerate(self.data):
                if idx:
                    curr = (each-self.data[idx-1])>>1
                    if curr>dist:
                        dist = curr
                        pos = self.data[idx-1] + dist
            curr = self.cap-1 - self.data[-1]
            if curr>dist:
                pos = self.cap - 1
            
        bisect.insort(self.data, pos)
        return pos

    def leave(self, p: int) -> None:
        self.data.remove(p)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)
