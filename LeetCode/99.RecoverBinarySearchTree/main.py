from Solution import *

if __name__ == '__main__':
	solution = Solution()

	root5 = TreeNode(4)
	root5.left = TreeNode(3)
	root5.left.left = TreeNode(1)
	root5.left.left.left = TreeNode(2)
	solution.recoverTree(root5) 

	print 

	root7 = TreeNode(146)
	root7.left = TreeNode(71)
	root7.right = TreeNode(-13)
	root7.left.left = TreeNode(55)
	root7.left.left.left = TreeNode(321)
	root7.left.left.left.left = TreeNode(-33)
	root7.right.left = TreeNode(231)
	root7.right.right = TreeNode(399)
	solution.recoverTree(root7) 

	print 

	root = TreeNode(7)
	root.left = TreeNode(2)
	root.left.left = TreeNode(1)
	root.left.right = TreeNode(9)
	root.left.right.left = TreeNode(3)
	root.left.right.left.right = TreeNode(4)
	root.left.right.right = TreeNode(6)
	root.right = TreeNode(5)

	solution.recoverTree(root)

	print 

	root2 = TreeNode(2)
	root2.right = TreeNode(1)
	solution.recoverTree(root2)

	print 

	root3 = TreeNode(1)
	root3.left = TreeNode(2)
	root3.right = TreeNode(3)
	solution.recoverTree(root3) 

	print 

	root4 = TreeNode(0)
	root4.left = TreeNode(2)
	root4.right = TreeNode(-5)
	solution.recoverTree(root4) 

	print 

	root6 = TreeNode(1)
	root6.left = TreeNode(3)
	root6.left.left = TreeNode(2)
	root6.left.left.left = TreeNode(4)
	solution.recoverTree(root6) 

	print 
	root8 = TreeNode(3)
	root8.left = TreeNode(4)
	root8.left.left = TreeNode(2)
	root8.left.left.left = TreeNode(1)
	solution.recoverTree(root8) 
