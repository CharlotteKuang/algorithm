# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
	def copyRandomList(self, head):
		"""
		:type head: RandomListNode
		:rtype: RandomListNode
		""" 
		if not head: return None

		p = head
		while p:
			tmp = p.next
			p.next = RandomListNode(p.val)
			p.next.random = p.random
			p.next.next = tmp
			p = tmp
		
		p = head
		while p:
			if p.random:
				p.next.random = p.random.next

		p = head
		rest = head.next
		while p:
			new_p = p.next
			
		rst = head.next 
