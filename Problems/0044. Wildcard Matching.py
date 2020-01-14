class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        self.mem = {}
        return self.match(s, p)
    
    def match(self, s, p):
        if (s, p) in self.mem:
            return self.mem[s, p]
        if not s and not p:
            self.mem[s, p] = True
            return True
        if not p:
            self.mem[s, p] = False
            return False
        if not s:
            for ch in p:
                if ch!='*':
                    self.mem[s, p] = False
                    return False
            self.mem[s, p] = True
            return True
        
        curr_match = s and (s[0]==p[0] or p[0]=='?')
        if p[0]=='*':
            self.mem[s, p] = self.match(s, p[1:]) or self.match(s[1:], p)
        else:
            self.mem[s, p] = curr_match and self.match(s[1:], p[1:])
        return self.mem[s, p]
