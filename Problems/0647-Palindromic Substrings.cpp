class Solution {
public:
    int countSubstrings(string s) {
        const int n = s.size();
        bool dp[n][n] = {0};
        int ret = 0;
        for(int plus=0; plus<n; plus++)
            for(int i=0; i<n-plus; i++){
                int j = i + plus;
                if(i==j){
                    ret++;
                    dp[i][j] = true;
                }
                else if(i==j-1)
                    if(s[i]==s[j]){
                        dp[i][j] = true;
                        ret++;
                    }
                    else
                        dp[i][j] = false;
                else if(s[i]==s[j] && dp[i+1][j-1]){
                    dp[i][j] = true;
                    ret++;
                }
            }
        return ret;
            
    }
};
