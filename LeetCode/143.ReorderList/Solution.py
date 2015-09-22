import pdb
# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def reorderList(self, head):
		"""
		:type head: ListNode
		:rtype: void Do not return anything, modify head in-place instead.
		""" 
		if not head: return
		p1 = head
		p2 = head
		halfTail = None

		while p2.next:
			halfTail = p1
			p1 = p1.next
			p2 = p2.next
			if p2.next:
				p2 = p2.next 

		reorderLinkedList = None
		p = p1 
		while p:
			tmp = p.next
			p.next = reorderLinkedList 
			reorderLinkedList = p
			p = tmp 

		p = reorderLinkedList
		origin = head
		while p:
			tmp = origin.next
			tmp_r = p.next
			origin.next = p
			p.next = tmp	
			p = tmp_r
			origin = tmp

		if origin: origin.next = None

def makeList(values):
	if len(values) == 0: return None
	if len(values) == 1: return ListNode(values[0])
	head = ListNode(values[0])
	p = head
	for i in values[1:]:
		p.next = ListNode(i)	
		p = p.next
	return head

def printList(l):
	result = []
	while l:
		result.append(str(l.val))
		l = l.next
	print 'list: ' , '-->'.join(result)

if __name__ == '__main__':
	l = makeList([1,2,3,4,5,6,7])
	sol = Solution()
	sol.reorderList(l)
	printList(l)

	l2 = makeList([1,2,3,4,5,6])
	sol.reorderList(l2)
	printList(l2)

	l3 = makeList([1,2])
	sol.reorderList(l3)
	printList(l3)

	l4 = makeList([])
	sol.reorderList(l4)
	printList(l4)
