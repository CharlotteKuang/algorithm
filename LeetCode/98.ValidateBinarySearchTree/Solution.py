import pdb
# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def inorderTraversalGenerator(self, node):
		if node.left: 
			for i in self.inorderTraversalGenerator(node.left):
				yield i
		if node: yield node.val
		if node.right: 
			for i in self.inorderTraversalGenerator(node.right):
				yield i
	# @param {TreeNode} root
	# @return {boolean}
	def isValidBST(self, root):
		if not root: return True
		result = list(self.inorderTraversalGenerator(root))		
		pdb.set_trace()
		for i in range(1, len(result)):
			if result[i-1] >= result[i]: return False
		return True

if __name__ == '__main__':
	root = TreeNode(10)
	root.left = TreeNode(5)
	root.right = TreeNode(15)
	root.right.right = TreeNode(6)
	root.right.right.left = TreeNode(20)

	solution = Solution()

	print solution.isValidBST(root)

	root = TreeNode(2)
	root.left = TreeNode(1)
	root.right = TreeNode(3)
	print solution.isValidBST(root)
