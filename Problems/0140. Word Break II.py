class Solution:
    def __init__(self):
        self.mem = {}
    
    def dfs(self, s, wordDict, idx):
        if idx in self.mem:
            return self.mem[idx]
        ret = []
        if idx==len(s):
            ret.append('')
        for i in range(idx+1, len(s)+1):
            curr = s[idx:i]
            if curr in wordDict:
                tmp = self.dfs(s, wordDict, i)
                for each in tmp:
                    if each:
                        ret.append(curr+' '+each)
                    else:
                        ret.append(curr)
        self.mem[idx] = ret
        return ret
    
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        return self.dfs(s, wordDict, 0)
