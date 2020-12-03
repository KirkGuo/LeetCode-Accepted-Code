class Solution:

    def __init__(self, nums: List[int]):
        self.map = collections.defaultdict(list)
        for idx, num in enumerate(nums):
            self.map[num].append(idx)

    def pick(self, target: int) -> int:
        n = len(self.map[target])
        return self.map[target][int(random.random() * n)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
