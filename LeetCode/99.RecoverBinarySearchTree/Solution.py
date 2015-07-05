import pdb
#Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def passTree(self, root):
		if root:	
			if root.left:
				for node in self.passTree(root.left):
					yield node
			yield root
			if root.right:
				for node in self.passTree(root.right):
					yield node
				
	# @param {TreeNode} root
	# @return {void} Do not return anything, modify root in-place instead.
	def recoverTree(self, root): 
		first, second, third = None, None, None
		node1, node2 = None, None
		count = 0
		for n in self.passTree(root):
			if node1 and node2: break
			if count == 0:
				first, second, third = n, None, None
			if count == 1:
				first, second, third = first, n, None
			if count == 2:
				first, second, third = first, second, n
			if count > 2:
				first, second, third = second, third, n
			count += 1
			if first and second and third:
				if first.val > second.val > third.val:
					node1, node2 = first, third
					break
				if first.val < third.val and first.val > second.val: 
					node1, node2 = first, second
					break
				if second.val < third.val and first.val > third.val:
					if not node1: node1 = first 
					elif first != node1: node2 = first 
				if first.val < third.val and (first.val > second.val or third.val < second.val):
					if not node1: node1 = second
					else: node2 = second
					continue
				if first.val < second.val and third.val < second.val:
					if not node1: node1 = third 
					else: node2 = third 
					continue

		if count < 3 and first.val > second.val:
			first.val, second.val = second.val, first.val
		if count == 3:
			tmp = [first.val, second.val, third.val]
			tmp.sort()
			first.val, second.val, third.val = tmp
		if count > 3:
			if node1 and node2:
				node1.val, node2.val = node2.val, node1.val
			elif second.val > third.val: third.val, second.val = second.val, third.val
		for n in self.passTree(root):
			print n.val
