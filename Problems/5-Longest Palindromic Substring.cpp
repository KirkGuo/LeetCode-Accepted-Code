class Solution {
public:
    string longestPalindrome(string s) {
        if(s.size()<2)
            return s;
        const int n = s.size();
        int dp[n][n] = {0};
        string ret;
        for(int m=0; m<n; m++)
            for(int i=0; i<n; i++){
                int j = i + m;
                if(j>=n)
                    break;
                if(i==j)
                    dp[i][j] = 1;
                else if(i==j-1)
                    dp[i][j] = s[i]==s[j]? 2 : 0;
                else
                    dp[i][j] = s[i]==s[j]? (dp[i+1][j-1]?dp[i+1][j-1]+2:0) : 0;
                if(dp[i][j]>ret.size())
                    ret = s.substr(i, dp[i][j]);
            }
        return ret;
    }
};
