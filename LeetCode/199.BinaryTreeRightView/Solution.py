# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def rightSideView(self, root):
        result = []
        if root:
            queue = [root, None]
            while len(queue):
                top = queue.pop(0)
                if not top:
                    continue
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)
                if len(queue) and not queue[0]:
                    result.append(top.val)
                    queue.append(None)
        return result