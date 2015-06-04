from Solution import * 

def main():
	solution = Solution()
	tree = TreeNode(1)
	tree.right = TreeNode(3)
	tree.left = TreeNode(2)
	tree.left.right = TreeNode(5)
	tree.left.left = TreeNode(4)

	newTree = solution.upsideDownBinaryTree(tree)
	print solution.preorderTraversal(newTree)
	print solution.inorderTraversal(newTree)
	
	tree.left.left.left = TreeNode(6)
	tree.left.left.right = TreeNode(7)
	newTree = solution.upsideDownBinaryTree(tree)
	print solution.preorderTraversal(newTree)
	print solution.inorderTraversal(newTree)

main()
