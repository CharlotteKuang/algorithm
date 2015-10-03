import pdb
# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def deleteDuplicates(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		if not head or not head.next: return head
		p = head
		rst = None
		pre = None
		while p:
			nextNode = p.next
			if nextNode and nextNode.val == p.val:
				v = p.val
				while p and p.val == v:
					tmp = p.next
					del(p)
					p = tmp
			else:
				if not rst: 
					rst = p
				else: 
					pre.next = p
				pre = p
				p = p.next
		if pre: pre.next = None
		return  rst

if __name__ == '__main__':
	head = ListNode(1)
	head.next = ListNode(2)
	head.next.next = ListNode(2)
	head.next.next.next = ListNode(3)

	sol = Solution()
	newHead = sol.deleteDuplicates(head)

	p = newHead
	while p:
		print p.val
		p = p.next
