class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxDepth(self, root):
        if root is None: return 0
        if root.left is None and root.right is None: return 1
        leftHeight = self.maxDepth(root.left)
        rightHeight = self.maxDepth(root.right)
        return 1 + max(leftHeight, rightHeight)