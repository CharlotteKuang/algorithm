# Definition for a binary tree node.
class TreeNode(object):
	 def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Codec: 
	def serialize(self, root):
		"""Encodes a tree to a single string.
		
		:type root: TreeNode
		:rtype: str
		"""
		rst = []
		if root:
			q = [root]
			rst.append(str(root.val))
			while q:	
				cur = q.pop(0)
				if cur.left:
					q.append(cur.left)
					rst.append(str(cur.left.val))
				else:
					rst.append('#')
				if cur.right:
					q.append(cur.right)
					rst.append(str(cur.right.val))
				else:
					rst.append('#')
			while rst and rst[-1] == '#':
				rst.pop()
		return ','.join(rst)

	def deserialize(self, data):
		"""Decodes your encoded data to tree.
		
		:type data: str
		:rtype: TreeNode
		"""
		if not data: return None

		arr = data.split(',')
		nodes = []	
		for i in range(len(arr)):
			if arr[i] == '#': 
				node = None
			else:
				node = TreeNode(int(arr[i]))
			nodes.append(node)
		childPos = 1
		for i in range(len(nodes)):
			if not nodes[i]: continue
			if childPos < len(nodes):
				nodes[i].left = nodes[childPos]
				childPos += 1
			if childPos < len(nodes):
				nodes[i].right = nodes[childPos]
				childPos += 1
		return 	nodes[0]	

# Your Codec object will be instantiated and called as such:
if __name__ == '__main__':
	codec = Codec()
	'''
	tree = TreeNode(1)
	tree.left = TreeNode(2)
	tree.right = TreeNode(3)
	tree.right.left = TreeNode(4)
	tree.right.right = TreeNode(5)
	[5,2,3,null,null,2,4,3,1]
	'''
	tree = TreeNode(1)
	tree.left = TreeNode(2)
	tree.right = TreeNode(3)
	tree.right.left = TreeNode(2)
	tree.right.right = TreeNode(4)
	tree.right.left.left = TreeNode(3)
	tree.right.left.right = TreeNode(1)
	print codec.serialize(tree)
	print codec.serialize(codec.deserialize(codec.serialize(tree)))
#codec.deserialize(codec.serialize(root))
