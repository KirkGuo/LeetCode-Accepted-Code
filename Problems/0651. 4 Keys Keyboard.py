class Solution:
    def maxA(self, N: int) -> int:
        if N<=5:
            return N;
        dp = [0 for i in range(N+1)]
        for i in range(6):
            dp[i] = i 
        for step in range(6, N+1):
            for mul in range(2, 6):
                dp[step] = max(dp[step], dp[step-mul-1]*mul)
            dp[step] = max(dp[step], dp[step-1]+1)
        return dp[N]
        
        
