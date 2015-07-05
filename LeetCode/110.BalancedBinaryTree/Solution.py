class Solution:
    def diffHeight(self, node):
        if node is None: return (0, True)
        
        leftBalanced = self.diffHeight(node.left)
        if not leftBalanced[1]: return (0, False)
        
        rightBalanced = self.diffHeight(node.right)
        if not rightBalanced[1]: return (0, False)
        
        if abs(leftBalanced[0] - rightBalanced[0]) > 1:
            return (0, False)
        else: return (max(leftBalanced[0], rightBalanced[0])+1, True)
    
    # @param {TreeNode} root
    # @return {boolean}
    def isBalanced(self, root):
        return (self.diffHeight(root))[-1]