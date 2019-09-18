class Solution {
public:
    int countBinarySubstrings(string s) {
        int cnt = 0;
        vector<int> groups;
        for(int i=0; i<s.size(); i++)
            if(i==0 || s[i]==s[i-1])
                cnt++;
            else{
                groups.push_back(cnt);
                cnt = 1;
            }
        groups.push_back(cnt);
        cnt = 0;
        for(int i=0; i<groups.size()-1; i++)
            cnt += min(groups[i], groups[i+1]);
        return cnt;
    }
};
