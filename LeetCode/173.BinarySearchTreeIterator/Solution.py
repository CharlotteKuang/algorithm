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

def iterateTree(node):
	# Your BSTIterator will be called like this:
	i, v = BSTIterator(node), []
	while i.hasNext(): v.append(i.next())
	print v 

root = TreeNode(6) 
iterateTree(root)

root.left = TreeNode(3) 
root.right = TreeNode(7)
iterateTree(root)

root.left.left = TreeNode(2) 
root.left.right = TreeNode(4) 
root.right = TreeNode(8)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
iterateTree(root)
