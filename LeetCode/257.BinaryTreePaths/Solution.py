# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def path_helper(self, node):
        if node:
            if not node.left and not node.right:
                yield str(node.val)
            if node.left:
                for s in self.path_helper(node.left):
                    yield str(node.val) + '->' + s
            if node.right:
                for s in self.path_helper(node.right):
                    yield str(node.val) + '->' + s
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root: return []
        return list(self.path_helper(root))
