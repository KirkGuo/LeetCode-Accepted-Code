class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        
        if d > n or d < 1:
            return -1
        if d == n:
            return sum(jobDifficulty)
        
        dp = [[float('inf') for _ in range(d+1)] for _ in range(n+1)]
        
        dp[0][0] = 0
        
        for i in range(1, n+1):
            for j in range(1, d+1):
                if i == j:
                    dp[i][j] = dp[i-1][j-1] + jobDifficulty[i-1]
                else:
                    curr_diff = jobDifficulty[i-1]
                    for k in range(i-1, j-2, -1):
                        curr_diff = max(curr_diff, jobDifficulty[k])
                        dp[i][j] = min(dp[i][j], dp[k][j-1] + curr_diff)
        return dp[n][d]
        
