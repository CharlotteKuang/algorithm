import pdb
# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param {TreeNode} root
	# @return {integer[][]}
	def levelOrder(self, root): 
		q = []
		result = []
		if root:
			q.append(None)
			q.append(root)
			while len(q):
				cur = q.pop(0) 
				if not cur:
					if len(q):
						result.append([])
						q.append(None)
				else:
					result[-1].append(cur.val)
					if cur.left:
						q.append(cur.left)
					if cur.right:
						q.append(cur.right)
		return result


if __name__ ==  '__main__':
	solution = Solution()

	root = TreeNode(1)
	root.left = TreeNode(2)
	root.right = TreeNode(3) 

	print solution.levelOrder(root)

	root.left.left = TreeNode(4)
	print solution.levelOrder(root)

	root.left.right = TreeNode(5)
	print solution.levelOrder(root)

	print solution.levelOrder(None)
