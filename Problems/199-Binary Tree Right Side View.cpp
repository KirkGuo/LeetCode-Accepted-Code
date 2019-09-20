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
    static void view(TreeNode* root, vector<int>& views, int dep){
        if(root==NULL)
            return;
        if(dep>views.size())
            views.push_back(root->val);
        else
            views[dep-1] = root->val;
        view(root->left, views, dep+1);
        view(root->right, views, dep+1);
        return;
    }
    vector<int> rightSideView(TreeNode* root) {
        vector<int> ret;
        view(root, ret, 1);
        return ret;
    }
};
