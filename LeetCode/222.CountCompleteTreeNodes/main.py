from Solution import *

def main():
	solution = Solution()

	root5 = TreeNode(1)
	root5.left = TreeNode(2) 
	root5.right = TreeNode(3) 
	root5.left.left = TreeNode(4)
	root5.left.right = TreeNode(5)
	print 'The count is :', solution.countNodes(root5)

	root6 = TreeNode(1)
	root6.left = TreeNode(2) 
	root6.right = TreeNode(3) 
	root6.left.left = TreeNode(4)
	root6.left.right = TreeNode(5)
	root6.right.left = TreeNode(6)
	print 'The count is :', solution.countNodes(root6)

	root7 = TreeNode(1)
	root7.left = TreeNode(2) 
	root7.right = TreeNode(3) 
	root7.left.left = TreeNode(4)
	root7.left.right = TreeNode(5)
	root7.right.left = TreeNode(6)
	root7.right.right = TreeNode(7)
	print 'The count is :', solution.countNodes(root7)

	root8 = TreeNode(1)
	root8.left = TreeNode(2) 
	root8.right = TreeNode(3) 
	root8.left.left = TreeNode(4)
	root8.left.right = TreeNode(5)
	root8.right.left = TreeNode(6)
	root8.right.right = TreeNode(7)
	root8.left.left.left = TreeNode(8)
	root8.left.left.right = TreeNode(9)
	root8.left.right.left = TreeNode(10)
	root8.left.right.right = TreeNode(11)
	print 'The count is :', solution.countNodes(root8)

	root = TreeNode(1)
	print 'The count is :', solution.countNodes(root)

	root2 = TreeNode(1)
	root2.left = TreeNode(2) 
	print 'The count is :', solution.countNodes(root2)

	root3 = TreeNode(1)
	root3.left = TreeNode(2) 
	root3.right = TreeNode(3) 
	print 'The count is :', solution.countNodes(root3)

	root4 = TreeNode(1)
	root4.left = TreeNode(2) 
	root4.right = TreeNode(3) 
	root4.left.left = TreeNode(4)
	print 'The count is :', solution.countNodes(root4) 

if __name__ == '__main__':
	main()
