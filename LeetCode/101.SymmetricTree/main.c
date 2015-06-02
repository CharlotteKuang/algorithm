/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool isRecursiveSymmetric(struct TreeNode* node1, struct TreeNode* node2) {
    if(node1 == NULL && node2 != NULL || node1 != NULL && node2 == NULL) {
        return false;
    }
    if(node1 == NULL && node2 == NULL) {
        return true;
    }
    if(node1->val != node2->val) {
        return false;
    }
    bool sideResult;
    sideResult = isRecursiveSymmetric(node1->left, node2->right);
    if(!sideResult) {
        return false;
    }
    sideResult = isRecursiveSymmetric(node1->right, node2->left);
    if(!sideResult) {
        return false;
    }
    return true;
}

bool isSymmetric(struct TreeNode* root) {
    if(root == NULL) return true;
    return isRecursiveSymmetric(root->left, root->right);
}