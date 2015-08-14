# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root:
            q = [root, None]
            while len(q) > 1:
                cur = q.pop(0)
                ne = q[0]
                cur.next = ne
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                if not ne:
                    q.pop(0)
                    q.append(None)
            q.pop()
