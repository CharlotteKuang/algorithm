# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recursiveSumNumbers(self, node, s):
        if not node: return 0
        
        v = node.val
        rst = 0
        if not node.left and not node.right: return s*10+v
        if node.left:
            rst += self.recursiveSumNumbers(node.left, s*10+v)
        if node.right:
            rst += self.recursiveSumNumbers(node.right, s*10+v)
        return rst
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.recursiveSumNumbers(root, 0) 
        
