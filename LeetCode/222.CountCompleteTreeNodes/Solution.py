import pdb
# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	'''
	def flip(self, num, times):
		result = 0
		for i in range(times):
			result <<= 1
			result += num & 1 
			num >>= 1
		return result

	# @param {TreeNode} root
	# @return {integer}
	def countNodes(self, root):
		height = 0	
		cur = root
		while cur:
			height += 1
			cur = cur.left
		if height <= 1: return height 
		
		tmp = 0
		cur = root
		while cur:
			tmp += 1
			cur = cur.right
		if tmp == height: return (1 << height) - 1

		head = 0
		tail = (1 << (height - 1)) -1 #node tail is always None
		
		#pdb.set_trace()
		while head + 1 < tail:
			mid = (head+tail)/2
			cur = root
			count = self.flip(mid, height-1)
			for i in range(height-1):
				if count & 1: cur = cur.right
				else: cur = cur.left
				count >>= 1
			if cur is None: tail = mid
			else: head = mid
		return (1 << height-1) + head 
	'''

	def height(self, node):
		cur = node
		result = 0
		while cur:
			result += 1
			cur = cur.left
		return result

	# @param {TreeNode} root
	# @return {integer}
	def countNodes(self, root):
		hroot = self.height(root)
		if hroot == 0: return 0
		hright = self.height(root.right)
		if hright == hroot - 1: return (1 << hroot - 1) + self.countNodes(root.right)
		else: return (1 << hright) + self.countNodes(root.left)
