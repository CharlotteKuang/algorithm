from Solution import BSTIterator
from Solution import TreeNode

def iterateTree(node):
	# Your BSTIterator will be called like this:
	i, v = BSTIterator(node), []
	while i.hasNext(): v.append(i.next())
	print v 

root = TreeNode(6) 
iterateTree(root)

root.left = TreeNode(3) 
root.right = TreeNode(7)
iterateTree(root)

root.left.left = TreeNode(2) 
root.left.right = TreeNode(4) 
root.right = TreeNode(8)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
iterateTree(root)
