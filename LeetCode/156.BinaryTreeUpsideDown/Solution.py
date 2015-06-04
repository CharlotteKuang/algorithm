# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def recursiveUpsideDown(self, node):
		if not node.left:
			self.newNode = TreeNode(node.val)
			return self.newNode 
		father = self.recursiveUpsideDown(node.left)
		if node.right:
			father.left = TreeNode(node.right.val)
		father.right = TreeNode(node.val)
		return father.right

	# @param {TreeNode} root
	# @return {TreeNode}
	def upsideDownBinaryTree(self, root): 
		if root:
			self.recursiveUpsideDown(root)
			return self.newNode
		else: return None

	def postorderTraversalGenerator(self, node):
		if node.left: 
			for i in self.postorderTraversalGenerator(node.left):
				yield i
		if node.right: 
			for i in self.postorderTraversalGenerator(node.right):
				yield i
		if node: yield node.val

    # @param {TreeNode} root
    # @return {integer[]}
	def postorderTraversalFunc(self, root):
		return list(self.postorderTraversalGenerator(root))

	def inorderTraversalGenerator(self, node):
		if node.left: 
			for i in self.inorderTraversalGenerator(node.left):
				yield i
		if node: yield node.val
		if node.right: 
			for i in self.inorderTraversalGenerator(node.right):
				yield i

    # @param {TreeNode} root
    # @return {integer[]}
	def inorderTraversalFunc(self, root):
		return list(self.inorderTraversalGenerator(root))

	def preorderTraversalGenerator(self, node):
		if node: yield node.val
		if node.left: 
			for i in self.preorderTraversalGenerator(node.left):
				yield i
		if node.right: 
			for i in self.preorderTraversalGenerator(node.right):
				yield i

    # @param {TreeNode} root
    # @return {integer[]}
	def preorderTraversalFunc(self, root):
		return list(self.preorderTraversalGenerator(root))

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
	# @param {TreeNode} root
	# @return {integer[]}
	def inorderTraversal(self, root):
		result = []
		s = []
		if root: s.append(root)
		while len(s):
			top = s[-1]
			while top.left:
				s.append(top.left)
				top = top.left
			while not top.right:
				result.append(top.val)
				s.pop()
				if len(s): top = s[-1]
				else:
					top = None
					break
			if top: 
				result.append(top.val)
				s.pop(-1)
				s.append(top.right)
		return result

	# @param {TreeNode} root
	# @return {integer[]}
	def postorderTraversal(self, root):
		result = []
		s = []
		if root: s.append(root)
		while len(s):
			top = s[-1]
			if not top.left and not top.right:
				result.append(top.val)
				s.pop()
				while len(s):
					tmp = s[-1]
					if tmp.left == top or tmp.right == top:
						result.append(tmp.val)
						top = s.pop(-1)
					else:
						break
			else:
				if top.right:
					s.append(top.right)
				if top.left:
					s.append(top.left)
		return result 
