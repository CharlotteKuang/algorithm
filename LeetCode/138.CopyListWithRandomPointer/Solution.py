import pdb
# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
	def __init__(self, x):
		self.label = x
		self.next = None
		self.random = None

class Solution(object):
	def copyRandomList(self, head):
		pdb.set_trace()
		"""
		:type head: RandomListNode
		:rtype: RandomListNode
		""" 
		if not head: return None

		p = head
		while p:
			tmp = p.next
			p.next = RandomListNode(p.label)
			p.next.random = p.random
			p.next.next = tmp
			p = tmp
		
		p = head
		while p:
			if p.random:
				p.next.random = p.random.next
			p = p.next.next

		p = head
		rst = head.next
		while p:
			new_p = p.next
			p.next = new_p.next	
			if p.next:
				new_p.next = p.next.next
			p = p.next
		return rst

if __name__ == '__main__':
	node = RandomListNode(1)

	sol = Solution()
	sol.copyRandomList(node)
