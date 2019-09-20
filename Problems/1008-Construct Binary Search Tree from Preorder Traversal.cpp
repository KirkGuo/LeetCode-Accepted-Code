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
    static TreeNode* insert(TreeNode* root, int val){
        if(root==NULL)
            return new TreeNode(val);
        if(root->val < val)
            root->right = insert(root->right, val);
        else
            root->left = insert(root->left, val);
        return root;
    }
    TreeNode* bstFromPreorder(vector<int>& preorder) {
        stack<TreeNode*> s;
        TreeNode* root=NULL;
        for(int each: preorder)
            root = insert(root, each);
        return root;
    }
};
