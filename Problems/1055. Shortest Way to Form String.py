class Solution:
    def __init__(self):
        self.mem = set()
    
    def isSubsqu(self, s, t):
        if t in self.mem:
            return True
        i = j = 0
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                i += 1
                j += 1
            else:
                i += 1
        if j==len(t):
            self.mem.add(t)
            return True
        return False
        
    def shortestWay(self, source: str, target: str) -> int:
        ans = 0
        curr = ''
        terminate = True
        idx = 0
        while True:
            curr += target[idx]
            if self.isSubsqu(source, curr):
                terminate = False
                idx += 1
                if idx==len(target):
                    ans += 1
                    break
            elif terminate:
                return -1
            else:
                terminate = True
                curr = ''
                ans += 1
        return ans
