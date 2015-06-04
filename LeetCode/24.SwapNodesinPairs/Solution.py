# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

def makeList(arr):
	if not arr: return None

	result = ListNode(arr[0])
	p = result
	for i in range(1, len(arr)):
		p.next = ListNode(arr[i])
		p = p.next
	return result

def printList(l):
	if not l: print None
	p = l
	while p:
		print p.val
		p = p.next
	print 

class Solution:
	# @param {ListNode} head
	# @return {ListNode}
	def swapPairs(self, head): 
		if not head or not head.next: return head

		p1 = head
		prev = None
		result = None
		while p1 and p1.next:
			p2 = p1.next
			tmp = p2.next
			p2.next = p1
			p1.next = tmp
			if prev:
				prev.next = p2
			else:
				head = p2
			prev = p1
			p1 = p1.next 
		return head 

