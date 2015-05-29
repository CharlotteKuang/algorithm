from Solution import Solution, TreeNode

def main():
	solution = Solution()

	test = TreeNode(0)
	test.left = TreeNode(1)
	test.left.left = TreeNode(2)
	test.left.left.left = TreeNode(3)
	print solution.inorderTraversal(test)
	print solution.postorderTraversal(test)

	test = TreeNode(0)
	#test.left 
	print solution.inorderTraversal(test)
	print solution.postorderTraversal(test)

	test = TreeNode(0)
	test.left = TreeNode(1)
	print solution.inorderTraversal(test)
	print solution.postorderTraversal(test)

	test = TreeNode(0)
	test.left = TreeNode(1)
	test.right = TreeNode(2)
	print solution.inorderTraversal(test) 
	print solution.postorderTraversal(test)

	test = TreeNode(0)
	test.left = TreeNode(1)
	test.right = TreeNode(2)
	test.right.left = TreeNode(3)
	print solution.inorderTraversal(test) 
	print solution.postorderTraversal(test)

main()
