from pdb import set_trace as debug

# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def reverseLinkedList(self, head, tail):
		if head is None or tail is None: return head 
		if head is tail: return head
		p1, p2 = head, head.next
		while p2 is not tail:
			tmp = p2.next
			p2.next = p1
			p1 = p2
			p2 = tmp
		tail.next = p1
		head.next = None
		return tail 

	# @param {ListNode} head
	# @return {boolean}
	def isPalindrome(self, head):

		if head is None or head.next is None: return True

		p1, p2, even = head, head, False
		while p2.next:		        
			p1 = p1.next
			p2 = p2.next
			if p2.next: p2 = p2.next 
			else: even = True

		if head.val != p2.val: return False

		halfMark = p1
		if even: halfTail = p1
		else: halfTail = p1.next
		lastHalf = self.reverseLinkedList(halfTail, p2)

		checkPos1, checkPos2, result = head, lastHalf, True
		while result and checkPos1 is not halfMark: 
			if checkPos1.val != checkPos2.val:
				result = False
			checkPos1 = checkPos1.next 
			checkPos2 = checkPos2.next

		self.reverseLinkedList(lastHalf, halfTail)

		return result
