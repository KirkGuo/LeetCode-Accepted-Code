class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        word2idx = {}
        for idx, each in enumerate(words):
            if each not in word2idx:
                word2idx[each] = []
            word2idx[each].append(idx)
        
        ans = -1
        i = j = 0
        while i < len(word2idx[word1]) and j < len(word2idx[word2]):
            idx1, idx2 = word2idx[word1][i], word2idx[word2][j]
            if idx1 > idx2:
                ans = idx1 - idx2 if ans == -1 else min(ans, idx1 - idx2)
                j += 1
            else:
                ans = idx2 - idx1 if ans == -1 else min(ans, idx2 - idx1)
                i += 1
        return ans
