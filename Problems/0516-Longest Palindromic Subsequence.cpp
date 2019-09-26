class Solution {
public:
    int longestPalindromeSubseq(string s) {
        const int n = s.size();
        int dp[n][n] = {0};
        int ret = 0;
        for(int plus=0; plus<n; plus++)
            for(int i=0; i<n-plus; i++){
                int j = i + plus;
                if(i==j){
                    dp[i][j] = 1;
                    ret = max(ret, dp[i][j]);
                }
                else if(i==j-1)
                    if(s[i]==s[j]){
                        dp[i][j] = 2;
                        ret = max(ret, dp[i][j]);
                    }
                    else
                        dp[i][j] = 1;
                else if(s[i]==s[j]){
                    dp[i][j] = dp[i+1][j-1]+2;
                    ret = max(ret, dp[i][j]);
                }
                else
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1]);
            }
        return ret;
    }
};
