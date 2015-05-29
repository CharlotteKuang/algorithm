# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def preorderTraversal(self, root):
        result = []
        if root:
            s = [root]
            while len(s):
                top = s.pop(-1)
                result.append(top.val)
                if top.right:
                    s.append(top.right)
                if top.left:
                    s.append(top.left)
        return result
	# @param {TreeNode} root
	# @return {integer[]}
	def inorderTraversal(self, root):
		result = []
		s = []
		if root: s.append(root)
		while len(s):
			top = s[-1]
			while top.left:
				s.append(top.left)
				top = top.left
			while not top.right:
				result.append(top.val)
				s.pop()
				if len(s): top = s[-1]
				else:
					top = None
					break
			if top: 
				result.append(top.val)
				s.pop(-1)
				s.append(top.right)
		return result

	# @param {TreeNode} root
	# @return {integer[]}
	def postorderTraversal(self, root):
		result = []
		s = []
		if root: s.append(root)
		while len(s):
			top = s[-1]
			if not top.left and not top.right:
				result.append(top.val)
				s.pop()
				while len(s):
					tmp = s[-1]
					if tmp.left == top or tmp.right == top:
						result.append(tmp.val)
						top = s.pop(-1)
					else:
						break
			else:
				if top.right:
					s.append(top.right)
				if top.left:
					s.append(top.left)
		return result 
