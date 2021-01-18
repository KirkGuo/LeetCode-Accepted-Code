class Solution:
    def __init__(self):
        self.mem = {}
        self.mod = int(1e9 + 7)

    def waysToDistribute(self, n: int, k: int) -> int:
        if n < k:
            return 0
        if k == 1:
            return 1
        if (n, k) in self.mem:
            return self.mem[n, k]
        self.mem[n, k] = (self.waysToDistribute(n-1, k-1) + self.waysToDistribute(n-1, k) * k) % self.mod
        
        return self.mem[n, k]
