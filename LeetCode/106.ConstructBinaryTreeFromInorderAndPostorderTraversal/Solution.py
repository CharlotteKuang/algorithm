from pdb import set_trace as db  

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def preorder(self, root):
		yield root.val 
		if root.left:
			for v in self.preorder(root.left):
				yield v
		if root.right:
			for v in self.preorder(root.right):
				yield v

	def inorder(self, root):
		if root.left:
			for v in self.preorder(root.left):
				yield v
		yield root.val 
		if root.right:
			for v in self.preorder(root.right):
				yield v

	#@param {integer[]} inorder 
	# @param {integer[]} postorder 
	# @return {TreeNode}
	def buildTree(self, inorder, postorder):
		self.keys = {}
		idx = 0
		for n in inorder:
			self.keys[n] = idx
			idx += 1
		return self.build(0, len(postorder)-1, postorder, 0, len(inorder)-1, inorder)

	def build(self, ph, pt, postorder, ih, it, inorder):
		#db()
		if ph > pt or ih > it: return None 

		root_val = postorder[pt]
		root = TreeNode(root_val)

		try: 
			idx = self.keys[root_val]
		except KeyError:
			return None
		
		l_len = idx-ih
		left_node = self.build(ph, ph+l_len-1, postorder, ih, ih+l_len-1, inorder)
		root.left = left_node
		
		right_node = self.build(ph+l_len, pt-1, postorder, idx+1, it, inorder)
		root.right = right_node

		return root

if __name__ == '__main__':
	solution = Solution()
	
	case = [
		([4,5,2,3,1], [4,2,5,1,3]),
		([1], [1]), 
		([1,2], [2,1]),
	]

	for c in case:
		postorder, inorder = c[0], c[1]
		root = solution.buildTree(inorder, postorder)
		pre = list(solution.preorder(root))
		inorder = list(solution.inorder(root))
		print pre
		print inorder 
