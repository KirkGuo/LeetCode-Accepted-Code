class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or '0'==s[0]:
            return 0
        dp = [1] + [0 for i in range(len(s))]
        for idx, each in enumerate(s, 1):
            if idx==1:
                dp[idx] = 1
                continue
            tstr = s[idx-2:idx]
            if tstr[1]=='0':
                if tstr[0] not in '12':
                    return 0
                else:
                    dp[idx] = dp[idx-2]
                continue
            if tstr in ['11','12','13','14','15','16','17','18','19','21','22','23','24','25','26']:
                dp[idx] = dp[idx-1] + dp[idx-2]
            else:
                dp[idx] = dp[idx-1]
        return dp[-1]
