class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck = sorted(deck, reverse=True)
        ret = []
        for idx, each in enumerate(deck):
            ret.append(each)
            ret = ret[1:] + [ret[0]] if idx != len(deck)-1 else ret
        return ret[::-1]
