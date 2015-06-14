# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param {TreeNode} root
	# @return {TreeNode}
	def invertTree(self, root):
		if root:
			tmp = root.right
			root.right = root.left
			root.left = tmp
			self.invertTree(root.left) #what about the returning result? useless!
			self.invertTree(root.right)
		return root

	# @param {TreeNode} root
	# @return {TreeNode}
	def invertTree2(self, root):
		if root:
			#make use of the returning result! fabulous
			root.left, root.right = self.invertTree2(root.right), self.invertTree2(root.left)
		return root
