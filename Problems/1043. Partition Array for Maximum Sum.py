class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        
        self.A = A
        self.K = K
        
        self.result = sum(A)
        self.mem = [0 for _ in A]
        
        self.helper()
        
        return self.result
    
    def helper(self):
        self.result = self.dfs(0)
        return
        
    def dfs(self, pos):
        if pos >= len(self.A):
            return 0
        
        if self.mem[pos]:
            return self.mem[pos]
        
        if pos == len(self.A) - 1:
            self.mem[pos] = self.A[pos]
            return self.mem[pos]
        
        pos_max = -1e8
        
        for i in range(self.K):
            length = i + 1
            if pos + length > len(self.A):
                continue
            curr_max = max(self.A[pos: pos+length])
            pos_max = max(pos_max, curr_max * length + self.dfs(pos+length))
        self.mem[pos] = pos_max
        return self.mem[pos]
        
        
