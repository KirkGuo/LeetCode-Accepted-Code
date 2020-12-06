class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        left = 0
        right = 0
        
        best = ''
        
        label = collections.Counter(t)
        word2idx = {k: v for v, k in enumerate(label.keys())}
        
        label = [label[key] for key in label.keys()]
        
        curr = [0 for each in label]
        
        for right, each in enumerate(s):
            if each not in word2idx:
                continue
            curr[word2idx[each]] += 1
            while self.valid(curr, label):
                if not best or right - left < best[1] - best[0]:
                    best = [left, right]
                remove_word = s[left]
                if remove_word in word2idx:
                    curr[word2idx[remove_word]] -= 1
                left += 1
        
        while self.valid(curr, label):
            if not best or right - left < best[1] - best[0]:
                best = [left, right]
            remove_word = s[left]
            if remove_word in word2idx:
                curr[word2idx[remove_word]] -= 1
            left += 1
        
        if not best:
            return best
        return s[best[0]: best[1]+1]
    
    def valid(self, hyp, ref):
        for a, b in zip(hyp, ref):
            if a < b:
                return False
        return True
        
        
        
                
