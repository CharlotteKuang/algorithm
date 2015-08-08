class Solution:
	# @param {TreeNode} root
	# @param {integer} sum
	# @return {boolean}
	def hasPathSum(self, root, sum):
		if not root: return False
		
		if not root.left and not root.right:
			return sum - root.val == 0
			
		if root.left:
			if self.hasPathSum(root.left, sum-root.val):
				return True
		if root.right:
			if self.hasPathSum(root.right, sum-root.val):
				return True
		
		return False
