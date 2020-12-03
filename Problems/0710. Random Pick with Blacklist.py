class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        self.w_len = N - len(blacklist)
        self.map = {}
        blacklist = set(blacklist)
        candi = N-1
        while candi in blacklist:
            candi -= 1
        for each in blacklist:
            if each < self.w_len:
                self.map[each] = candi
                candi -= 1
                while candi in blacklist:
                    candi -= 1

    def pick(self) -> int:
        index = int(self.w_len * random.random())
        if index in self.map:
            return self.map[index]
        return index


# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()
