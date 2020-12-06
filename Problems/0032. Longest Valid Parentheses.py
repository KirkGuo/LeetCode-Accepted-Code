class Solution:
    def longestValidParentheses(self, s: str) -> int:
        best = 0
        q = [-1]
        for idx, each in enumerate(s):
            if each == '(':
                q.append(idx)
            else:
                q.pop()
                if not q:
                    q.append(idx)
                else:
                    preIdx = q[-1]
                    best = max(best, idx - preIdx)
        
        return best
