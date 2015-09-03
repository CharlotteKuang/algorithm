import pdb
# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def rotateRight(self, head, k):
		"""
		:type head: ListNode
		:type k: int
		:rtype: ListNode
		""" 
		if not head: return

		l = 0
		p = head 
		while p:
			tail = p
			p = p.next
			l += 1

		k %= l
		if k == 0: return head
		p = head
		count = 1 
		pdb.set_trace()
		while count < l-k:
			p = p.next
			count += 1

		rotate_node = p.next
		p.next = None
		tail.next = head
		return rotate_node 

	def printList(self, head):
		rst = []
		p = head
		while p:
			rst.append(str(p.val))
			p = p.next
		print '->'.join(rst)

	def makeList(self, arr):
		head = ListNode(arr[0]) if len(arr) > 0 else None
		p = head
		for i in range(1, len(arr)):
			p.next = ListNode(arr[i])
			p = p.next
		return head

if __name__ == '__main__':
	sol = Solution()

	cases = [ ([1,2,3], 2), ([1,2,3,4,5], 3), ([], 3), ([1,3,4,6,7], 9), ([1,2,3], 3), ([1,2,3], 2000000000)]

	for case in cases:
		l = sol.makeList(case[0])
		rotate_l = sol.rotateRight(l, case[1])
		sol.printList(rotate_l)
