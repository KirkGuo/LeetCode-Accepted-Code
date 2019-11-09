class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int x = 0, y = 0;
        int dir_x[4] = {0, 1, 0, -1}, dir_y[4] = {1, 0, -1, 0};
        int idx = 0;
        vector<int> ans;
        if(!matrix.size())
            return ans;
        int n = matrix.size()*matrix[0].size();
        while(n--){
            ans.push_back(matrix[x][y]);
            matrix[x][y] = INT_MAX;
            int tmp_x = x + dir_x[idx];
            int tmp_y = y + dir_y[idx];
            if(tmp_x==matrix.size() || tmp_x==-1){
                idx = (idx+1) % 4;
                x += dir_x[idx];
                y += dir_y[idx];
                continue;
            }   
            else if(tmp_y==matrix[0].size() || tmp_y==-1){
                idx = (idx+1) % 4;
                x += dir_x[idx];
                y += dir_y[idx];
                continue;
            }   
            if(matrix[tmp_x][tmp_y]==INT_MAX){
                idx = (idx+1) % 4;
                x += dir_x[idx];
                y += dir_y[idx];
                continue;
            }
            x = tmp_x;
            y = tmp_y;
        }
        return ans;
    }
};
