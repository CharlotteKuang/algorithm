# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None
	def getListNode(self):
		p = self
		while p:
			print p.val
			p = p.next

class Solution:
	# @return a ListNode
	def addTwoNumbers(self, l1, l2):
		if l1 is None:
			return l2
		if l2 is None:
			return l1
		result = ListNode((l1.val + l2.val) % 10) 
		# I wrote the wrong condition(result.val >= 10)
		if l1.val + l2.val >= 10: flag = 1 
		else: flag = 0
		p1 = l1.next
		p2 = l2.next
		p3 = result
		while p1 is not None and p2 is not None:
			tmp = p1.val + p2.val + flag
			if tmp >= 10:
				flag = 1 
			else: flag = 0
			p3.next = ListNode(tmp % 10)
			p3 = p3.next	
			p1 = p1.next
			p2 = p2.next
		if p1 is None and p2 is None:
			if flag == 1:
				p3.next = ListNode(1)
		else:
			if p1: p = p1
			else: p = p2
			while p is not None:
				tmp = p.val + flag
				if tmp >= 10:
					flag = 1
				#forget to clear the flag
				else: flag = 0
				p3.next = ListNode(tmp % 10)
				p3 = p3.next
				p = p.next
			if flag == 1:
				p3.next = ListNode(1)
		return result	
