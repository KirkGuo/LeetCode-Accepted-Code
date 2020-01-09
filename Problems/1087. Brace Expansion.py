class Solution:
    def __init__(self):
        self.words = []
    
    def dfs(self, s, curr):
        if not s:
            if curr:
                self.words.append(curr)
            return
        
        if 'a'<=s[0]<='z':
            self.dfs(s[1:], curr+s[0])
        else:
            candi = []
            for idx, each in enumerate(s):
                if each=='}':
                    break
                if 'a'<=each<='z':
                    candi.append(each)
            for each in candi:
                self.dfs(s[idx+1:], curr+each)
        
    def expand(self, S: str) -> List[str]:
        self.dfs(S, '')
        return sorted(self.words)
