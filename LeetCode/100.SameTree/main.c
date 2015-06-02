/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool recursiveSameTree(struct TreeNode* p, struct TreeNode* q) {
    if(p == NULL && q != NULL || p != NULL && q == NULL) {
        return false;
    }
    if(p == NULL && q == NULL) {
        return true;
    }
    if(p->val == q->val) {
        bool leftResult = recursiveSameTree(p->left, q->left);
        if(!leftResult) {
            return false;
        }
        bool rightResult = recursiveSameTree(p->right, q->right);
        if(!rightResult) {
            return false;
        }
        return true;
    } else {
        return false;
    }
}

bool isSameTree(struct TreeNode* p, struct TreeNode* q) {
    return recursiveSameTree(p, q);
}
