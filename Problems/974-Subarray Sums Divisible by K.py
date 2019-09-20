class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        dp = collections.defaultdict(int)
        dp[0] = 1
        ret = 0
        s = 0
        for each in A:
            s += each
            if s%K in dp:
                ret += dp[s%K]
            dp[s%K] += 1
        return ret
