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
        curr_match = s and (s[0]==p[0] or p[0]=='.')
        if len(p)>=2 and p[1]=='*':
            self.mem[s, p] = self.match(s, p[2:]) or curr_match and self.match(s[1:], p)
        else:
            self.mem[s, p] = curr_match and self.match(s[1:], p[1:])
        return self.mem[s, p]
