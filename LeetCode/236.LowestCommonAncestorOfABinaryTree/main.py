from Solution import *

if __name__ == '__main__':
	solution = Solution()

	root = TreeNode(3)
	p = root.left = TreeNode(4)
	q = root.right = TreeNode(8)

	print solution.lowestCommonAncestor(root, p, q) == root
	print solution.lowestCommonAncestor(root, root, q) == root

	root = TreeNode(3)
	target = root.left = TreeNode(4)
	root.right = TreeNode(8)
	p = root.left.left = TreeNode(5)
	q = root.left.right = TreeNode(6)
	
	print solution.lowestCommonAncestor(root, p, q) == target

	target = root = TreeNode(3)
	root.left = TreeNode(4)
	p = root.right = TreeNode(8)
	root.left.left = TreeNode(5)
	q = root.left.right = TreeNode(6)
	
	print solution.lowestCommonAncestor(root, p, q) == target
