class Solution:
    def __init__(self):
        self.ans = set()
        self.min_removed = float("inf")
        
    
    def dfs(self, curr, s, left, right, removed):
        if not s:
            if left==right:
                if removed<self.min_removed:
                    self.ans = {curr}
                    self.min_removed = removed
                elif removed==self.min_removed:
                    self.ans.add(curr)
            
        else:
            if s[0]!='(' and s[0]!=')':
                self.dfs(curr+s[0], s[1:], left, right, removed)
            else:
                self.dfs(curr, s[1:], left, right, removed+1)
                if s[0]=='(':
                    self.dfs(curr+s[0], s[1:], left+1, right, removed)
                elif right<left:
                    self.dfs(curr+s[0], s[1:], left, right+1, removed)
                
    
    
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.dfs('', s, 0, 0, 0)
        return list(self.ans) if self.ans else ['']
