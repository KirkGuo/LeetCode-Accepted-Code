class Solution:    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        q = [0]
        visited = [0 for each in s]
        while q:
            curr = q.pop()
            if curr==len(s):
                return True
            if not visited[curr]:
                for each in wordDict:
                    l = len(each)
                    prefix = s[curr:l+curr]
                    remain = s[l+curr:]
                    if each==prefix:
                        q.append(l+curr)
                visited[curr] = 1
        return False
        
