class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        self.mem = {}
        
        ans = self.count(s, t)
        return ans
    
    def count(self, s, t):
        if len(s) < len(t):
            return 0
        if (s, t) in self.mem:
            return self.mem[s, t]
        
        if not s and not t:
            return 1
        
        if not t:
            return 1
        
        if s[0] == t[0]:
            self.mem[s, t] = self.count(s[1:], t[1:]) + self.count(s[1:], t)
            return self.mem[s, t]
        
        self.mem[s, t] = self.count(s[1:], t)
        return self.mem[s, t]
        
