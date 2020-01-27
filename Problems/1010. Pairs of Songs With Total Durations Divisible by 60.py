class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        mem = collections.defaultdict(int)
        ans = 0
        for each in time:
            remain = each%60
            comp = (60-remain)%60
            if comp in mem:
                ans += mem[comp]
            mem[remain] += 1
        return ans
