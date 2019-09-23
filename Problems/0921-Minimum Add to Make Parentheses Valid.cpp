class Solution {
public:
    int minAddToMakeValid(string S) {
        int ret = 0;
        int left = 0;
        for(int i=0; i<S.size(); i++)
            if(S[i]=='(')
                left++;
            else if(left==0)
                ret++;
            else
                left--;
        return ret + left;
    }
};
