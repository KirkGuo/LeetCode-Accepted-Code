class WordDistance:

    def __init__(self, words: List[str]):
        self.word2idx = collections.defaultdict(list)
        for idx, each in enumerate(words):
            self.word2idx[each].append(idx)

    def shortest(self, word1: str, word2: str) -> int:
        lst1, lst2 = self.word2idx[word1], self.word2idx[word2]
        idx1 = idx2 = 0
        ans = float("inf")
        while idx1<len(lst1) and idx2<len(lst2):
            ans = min(ans, abs(lst1[idx1]-lst2[idx2]))
            if lst1[idx1]<lst2[idx2]:
                idx1 += 1
            else:
                idx2 += 1
        return ans


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
