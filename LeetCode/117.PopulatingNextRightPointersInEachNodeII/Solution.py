# Definition for binary tree with next pointer.
class TreeLinkNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		self.next = None

class Solution:
	# @param root, a tree link node
	# @return nothing
	def connect(self, root):
		if root:
			if root.left and root.right:
				root.left.next = root.right
				if root.next:
					root.right.next = root.next.left
					self.connect(root.left)
					self.connect(root.right)

if __name__ == '__main__':
	sol = Solution()
	root = TreeLinkNode(1)
	root.left = TreeLinkNode(2)
	root.right = TreeLinkNode(3) 
	root.left.left = TreeLinkNode(4)
	root.left.right = TreeLinkNode(5)
	root.right.left = TreeLinkNode(6)
	root.right.right = TreeLinkNode(7)

	sol.connect(root)

	print root.right.left.next == root.right.right
