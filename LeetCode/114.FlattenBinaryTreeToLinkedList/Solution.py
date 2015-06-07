# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param {TreeNode} node 
	# @return {TreeNode} return the last node of the flattened tree.
	def recursiveFlatten(self, node):
		if node:
			left = node.left
			right = node.right
			tail = None
			if left:
				node.left = None
				node.right = left
				tail = self.recursiveFlatten(left)
			else:
				tail = node
			if right:
				tail.right = right
				tail = self.recursiveFlatten(right)
			return tail 
		else: return None

	# @param {TreeNode} root
	# @return {void} Do not return anything, modify root in-place instead.
	def flatten(self, root): 
		if root: self.recursiveFlatten(root)
