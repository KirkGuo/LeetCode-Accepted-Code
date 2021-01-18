class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        
        mem = {k:v for v, k in enumerate(row)}
        
        n = len(row)
        ans = 0
        
        for i in range(0, n, 2):
            target = self.find_couple(row[i])
            curr = row[i+1]
            if curr != target:
                ans += 1
                row[mem[curr]], row[mem[target]] = row[mem[target]], row[mem[curr]]
                mem[curr], mem[target] = mem[target], mem[curr]
                
        return ans
    
    def find_couple(self, i):
        if i & 1:
            return i - 1
        return i + 1
