# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def preorderTraversal(self, root):
        result = []
        if root:
            s = [root]
            while len(s):
                top = s.pop(-1)
                result.append(top.val)
                if top.right:
                    s.append(top.right)
                if top.left:
                    s.append(top.left)
        return result

