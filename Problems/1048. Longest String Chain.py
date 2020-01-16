class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        def isPred(x, y):
            if len(x)+1!=len(y):
                return False
            diff=0
            i = j = 0
            while i<len(x) and j<len(y):
                if x[i]!=y[j]:
                    diff += 1
                    j += 1
                else:
                    i += 1
                    j += 1
            return diff==1 or diff==0
        
        q = []
        links = collections.defaultdict(list)
        words = sorted(words, key=lambda x:(len(x), x))
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if isPred(words[i], words[j]):
                    links[words[i]].append(words[j])
                if len(words[j])-len(words[i])>1:
                    break
        ans = 1
        visited = set()
        for each in list(links):
            q.append((each, 1))
            while q:
                curr, length = q.pop(0)
                ans = max(ans, length)
                if curr in visited:
                    continue
                visited.add(curr)
                for item in links[curr]:
                    q.append((item, length+1))
            
        return ans
