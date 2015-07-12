//Lowest Common Ancestor of a Binary Search Tree
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* lowestCommonAncestor(struct TreeNode* root, struct TreeNode* p, struct TreeNode* q) {
    int min = p->val <= q->val ? p->val : q->val;
    int max = p->val > q->val ? p->val : q->val;
    if(root->val > min && root->val < max) {
        return root;
    }
    if(root->val == min || root->val == max) {
        return root->val == p->val ? p : q;
    }
    if(root->val > max) {
        return lowestCommonAncestor(root->left, p, q);
    } else {
        return lowestCommonAncestor(root->right, p, q);
    }
}