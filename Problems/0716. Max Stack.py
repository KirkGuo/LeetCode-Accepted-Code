class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        return None

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None

    def peekMax(self) -> int:
        if self.stack:
            return max(self.stack)
        return None

    def popMax(self) -> int:
        if not self.stack:
            return None
        curr, idx = self.stack[-1], len(self.stack)-1
        for i in range(len(self.stack)-1, -1, -1):
            if self.stack[i]>curr:
                curr, idx = self.stack[i], i
        self.stack = self.stack[:idx] + self.stack[idx+1:]        
        return curr
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
