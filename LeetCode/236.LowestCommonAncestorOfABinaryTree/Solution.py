# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param {TreeNode} root
	# @param {TreeNode} p
	# @param {TreeNode} q
	# @return {TreeNode}
	def lowestCommonAncestor(self, root, p, q): 
		def searchLCAwithInorder(rootNode, node1, node2):		
			isNode1Found = False
			isNode2Found = False

			if rootNode == node1: 
				#return (rootNode, True, False) can't solve the case lca == node1
				#the program should continue searchring for node2
				isNode1Found = True		
			if rootNode == node2: 
				#return (rootNode, False, True) can't solve the case lca == node2
				#the program should continue searchring for node1
				isNode2Found = True 

			if rootNode.left:
				lca, found1, found2 = searchLCAwithInorder(rootNode.left, p, q)
				if lca: return (lca, found1, found2) 
				isNode1Found, isNode2Found = found1 or isNode1Found, found2 or isNode2Found

			if rootNode.right:
				lca, found1, found2 = searchLCAwithInorder(rootNode.right, p, q)
				if lca: return (lca, found1, found2)
				isNode1Found, isNode2Found = found1 or isNode1Found, found2 or isNode2Found

			if isNode1Found and isNode2Found:
				return (rootNode, True, True) 
			else:
				return (None, isNode1Found, isNode2Found)

		result = searchLCAwithInorder(root, p, q)
		return result[0]
