/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int findMax(const vector<int>& nums, const int left, const int right){
        int max = nums[left];
        int ret = left;
        for(int i=left+1; i<=right; i++)
            if(nums[i]>max){
                max = nums[i];
                ret = i;
            }
        return ret;
    }
    TreeNode* constructMaximumBinaryTree(vector<int>& nums, int left=0, int right=INT_MAX) {
        if(right==INT_MAX) right = nums.size()-1;
        if(left>right) return nullptr;
        if(left==right) return new TreeNode(nums[left]);
        int idx = findMax(nums, left, right);
        TreeNode *root = new TreeNode(nums[idx]);
        root->left = constructMaximumBinaryTree(nums, left, idx-1);
        root->right = constructMaximumBinaryTree(nums, idx+1, right);
        return root;
    }
};
