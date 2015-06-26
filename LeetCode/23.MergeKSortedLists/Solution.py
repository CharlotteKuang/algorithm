import pdb
# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

# @param {[]} number list 
# @return {ListNode}
def makeList(arr):
	if not arr: return None
	result = ListNode(arr[0])
	p = result
	for num in arr[1:]:
		p.next = ListNode(num)
		p = p.next
	return result

def printList(node):
	p = node 
	while p and p.next:
		print p.val, '-->'
		p = p.next
	if p: print p.val

class Solution:
	# @param {ListNode[]} lists
	# @return {ListNode}
	# recursive merge sort.
	def mergeKLists(self, lists): 
		l = len(lists)
		if l == 0: return None
		if l == 1: return lists[0]

		mid = (l-1) / 2
		l1 = self.mergeKLists(lists[0:mid+1])
		l2 = self.mergeKLists(lists[mid+1:])

		p1 = l1
		p2 = l2
		head = None
		p = head
		while p1 and p2:
			if p1.val < p2.val:
				tmp = p1
				p1 = p1.next
			else:
				tmp = p2
				p2 = p2.next
			if head is None:
				head = tmp
				p = head
			else:
				p.next = tmp
				p = p.next
		
		if p is None:
			if p1: return p1
			else: return p2
		if p1 is None: p.next = p2
		else: p.next = p1
		
		return head
