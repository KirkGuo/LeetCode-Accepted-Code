class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        for(int i=1; i<matrix.size(); i++)
            for(int j=1; j<matrix[i].size(); j++)
                if(matrix[i][j]-'0')
                    matrix[i][j] = min(matrix[i-1][j], min(matrix[i-1][j-1], matrix[i][j-1])) + 1;
        int ans = 0;
        for(int i=0; i<matrix.size(); i++)
            for(int j=0; j<matrix[i].size(); j++)
                if(matrix[i][j]-'0' > ans)
                    ans = matrix[i][j]-'0';
        return ans*ans;       
    }
};
