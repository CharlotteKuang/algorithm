import pdb
# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def inorder(self, root):
		if not root: return
		if not root.left and not root.right:
			print root.val 
			return 
		if root.left:
			self.inorder(root.left)
		print root.val
		if root.right:
			self.inorder(root.right)

    # @param root, a tree node
    # @param head, a list node
    # @return a list node
	def buildTreeWithSortedList(self, root, head):
		if not root.left and not root.right:
			root.val = head.val
			return head.next
		
		if root.left:
			head = self.buildTreeWithSortedList(root.left, head)

		root.val = head.val
		head = head.next

		if root.right:
			head = self.buildTreeWithSortedList(root.right, head)

		return head
			
    # @param head, a list node
    # @return a tree node
	def sortedListToBST(self, head):
		if not head: return None

		#step2. build tree
		root = TreeNode(0)
		queue = [root]
		count = 1
		l = head.next
		while l:
			cur = queue.pop(0)
			if l:
				cur.left = TreeNode(0)
				queue.append(cur.left)
				l = l.next
			if l:
				cur.right = TreeNode(0)
				queue.append(cur.right)
				l = l.next

		#step3. use DFS to set the value of each tree node
		self.buildTreeWithSortedList(root, head)
		return root

if __name__ == '__main__':
	head = ListNode(1)
	head.next = ListNode(2)
	head.next.next = ListNode(3)

	sol = Solution()
	root = sol.sortedListToBST(head)
	sol.inorder(root)

	print
	head.next.next.next = ListNode(4)
	root = sol.sortedListToBST(head)
	sol.inorder(root)

	print
	head.next.next.next.next = ListNode(5)
	root = sol.sortedListToBST(head)
	sol.inorder(root)

	print
	head.next.next.next.next.next = ListNode(6)
	root = sol.sortedListToBST(head)
	sol.inorder(root)

	print
	root = sol.sortedListToBST(None)
	sol.inorder(root)
