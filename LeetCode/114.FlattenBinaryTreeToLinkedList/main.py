from Solution import *

def printFlattenTree(node):
	curNode = node
	while curNode:
		print curNode.val
		curNode = curNode.right

def main():
	root = TreeNode(1)
	root.left = TreeNode(2)
	root.left.left = TreeNode(3)
	root.left.right = TreeNode(4)
	root.right = TreeNode(5)
	root.right.right = TreeNode(6)
	
	solution = Solution()
	solution.flatten(root)
	printFlattenTree(root)

	print '----' 

	root2 = TreeNode(1)
	solution.flatten(root2)
	printFlattenTree(root2)

	print '----' 

	root3 = TreeNode(1)
	root3.right = TreeNode(2)
	root3.right.left = TreeNode(3)
	root3.right.right = TreeNode(4)
	root3.right.right.right = TreeNode(5)
	solution.flatten(root3)
	printFlattenTree(root3)

	print '----' 

	solution.flatten(None)
	printFlattenTree(None)

if __name__ == '__main__': main()

