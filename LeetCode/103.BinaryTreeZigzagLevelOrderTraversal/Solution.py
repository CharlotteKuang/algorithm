# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param {TreeNode} root
	# @return {integer[][]}
	def zigzagLevelOrder(self, root):
		if not root: return []

		result = []
		count = 1
		s = [root]				        
		while  len(s):
			tmp = []
			row = []
			while len(s):
				cur = s.pop()
				row.append(cur.val)
				if count % 2:
					if cur.left: tmp.append(cur.left)
					if cur.right: tmp.append(cur.right)
				else:
					if cur.right: tmp.append(cur.right)
					if cur.left: tmp.append(cur.left)
			count += 1
			s = tmp
			result.append(row)
		return result

if __name__ == '__main__':
	solution = Solution()
	root = TreeNode(1) 
	print solution.zigzagLevelOrder(root)
	
	root.left = TreeNode(2)
	print solution.zigzagLevelOrder(root)

	root.right = TreeNode(3)
	print solution.zigzagLevelOrder(root)

	root.left.left = TreeNode(4)
	print solution.zigzagLevelOrder(root)

	root.left.right = TreeNode(5)
	print solution.zigzagLevelOrder(root)

	root.right.right = TreeNode(6)
	root.right.left = TreeNode(7)
	print solution.zigzagLevelOrder(root)

	print solution.zigzagLevelOrder(None)
