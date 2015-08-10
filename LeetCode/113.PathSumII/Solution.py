# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param {TreeNode} root
	# @param {integer} sum
	# @return {integer[][]}
	def pathSum(self, root, sum):
		if not root: return []
		if not root.left and not root.right:
			if root.val == sum: return [[root.val]]
			else: return []

		result = []
		leftPath = self.pathSum(root.left, sum-root.val)
		for i in leftPath:
			i.insert(0, root.val)
			result.append(i)
		rightPath = self.pathSum(root.right, sum-root.val)
		for i in rightPath:
			i.insert(0, root.val)
			result.append(i)

		return result

if __name__ == '__main__':
	root = TreeNode(3)
	root.left = TreeNode(2)
	root.right = TreeNode(1)

	sol = Solution()

	print sol.pathSum(root, 4)
