# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorder(self, root):
        if root.left:
            for i in self.inorder(root.left):
                yield i
                
        yield root
        
        if root.right:
            for i in self.inorder(root.right):
                yield i
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        count = 0
        for elem in self.inorder(root):
            if count == k-1:
                return elem.val
            count += 1
