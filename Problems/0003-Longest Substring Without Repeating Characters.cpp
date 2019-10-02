class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int m[256];
        memset(m, -1, sizeof(m));
        int curr = 0;
        int ans = 0;
        int start = 0;
        for(int i=0; i<s.size(); i++){
            if(m[s[i]]<start){
                curr++;
                ans = max(curr, ans);
                m[s[i]] = i;
            }
            else{
                curr = i - m[s[i]];
                start = m[s[i]]+1;
                m[s[i]] = i;
            }
        }
        return ans;
    }
};
