class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ret = 0
        s = 0
        dp = collections.defaultdict(int)
        dp[0] = 1
        for each in nums:
            s += each
            if s-k in dp:
                ret += dp[s-k]
            dp[s] += 1
        return ret
