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
    static void treeWalk(TreeNode* root, vector<int>& sums, int lel){
        if(root==NULL)
            return;
         if(lel>sums.size())
            sums.push_back(root->val);
        else
            sums[lel-1] += root->val;
        Solution::treeWalk(root->left, sums, lel+1);
        Solution::treeWalk(root->right, sums, lel+1);
        return;
    }
    int maxLevelSum(TreeNode* root) {
        vector<int> sums;
        Solution::treeWalk(root, sums, 1);
        int idx = 1, curr = sums[0];
        for(int i=1; i<sums.size(); i++)
            if(sums[i]>curr){
                idx = i +1;
                curr = sums[i];
            }
        return idx;
    }
};
