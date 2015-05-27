import pdb
#Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

def makeList(array):
	result = None
	p = result
	for num in array:
		if not result:
			result = ListNode(num)
			p = result
		else:
			p.next = ListNode(num)
			p = p.next
	return result

def printList(ls):
	p = ls
	while p:
		print p.val, '->'
		p = p.next
	
class Solution:
	# @param {ListNode} head
	# @param {integer} n
	# @return {ListNode}
	def removeNthFromEnd(self, head, n):
		if head is None: return
		p1 = head
		p2 = head
		length = 0
		even = False
		while p1.next and p2.next: 
			p1 = p1.next	
			p2 = p2.next
			length += 1
			if not p2.next:
				even = True
				break
			p2 = p2.next
		if not even:
			length = length*2+1
		else: length = length*2
		#pdb.set_trace()
		count = length-n+1
		pre = None
		p = head
		for i in range(1, count):
			pre = p
			p = p.next
			count -= 1
		if not pre:
			tmp = head
			head = head.next
			del(tmp)
		else:
			pre.next = p.next
			del(p)
		return head
