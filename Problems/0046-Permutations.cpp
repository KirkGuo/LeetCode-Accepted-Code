class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> ans;
        int n = nums.size();
        sort(nums.begin(), nums.end());
        bool mark = true;
        while(mark){
            ans.push_back(nums);
            mark = next_permutation(nums.begin(), nums.end());
        }
        return ans;
    }
};
