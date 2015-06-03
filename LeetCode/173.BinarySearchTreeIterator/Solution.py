# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
	def __init__(self, root):
		self.__s__ = []        
		if root:
			self.__s__.append(root)
			cur = root.left
			while cur:
				self.__s__.append(cur)
				cur = cur.left

	def __del__(self):
		while self.__s__: s.pop()

    # @return a boolean, whether we have a next smallest number
	def hasNext(self):
		return len(self.__s__) > 0 

    # @return an integer, the next smallest number
	def next(self):
		if len(self.__s__):
			top = self.__s__.pop()
			if top.right:
				self.__s__.append(top.right)
				cur = top.right.left
				while cur:
					self.__s__.append(cur)
					cur = cur.left
			return top.val 
		else: return None 
