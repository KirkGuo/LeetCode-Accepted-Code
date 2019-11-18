class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alien2alpha = {}
        for idx, each in enumerate(order):
            alien2alpha[each] = chr(ord('a')+idx)
        alpha_words = [''.join(alien2alpha[letter] for letter in each) for each in words]
        tmp = sorted(alpha_words)
        for each1, each2 in zip(tmp, alpha_words):
            if each1 != each2:
                return False
        return True
