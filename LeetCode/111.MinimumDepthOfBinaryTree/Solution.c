/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int minDepth(struct TreeNode* root) {
    if(!root) return 0;
    if(!root->left && !root->right) return 1;
    int min = 10000;
    if(root->left) {
        min = minDepth(root->left);
        //minDepth = leftDepth;
    }
    if(root->right) {
        int rightDepth = minDepth(root->right);
        min = min <= rightDepth ? min : rightDepth;
    }
    return min + 1; 
}
