import pdb
# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def getIntersectionNode(self, headA, headB):
		"""
		:type head1, head1: ListNode
		:rtype: ListNode
		""" 
		if not headA or not headB: return None
		
		p = headA
		while p.next:
			p = p.next
		mark = p
		#make a cycled list
		mark.next = headA
		
		rst = None
		p1 = headB
		p2 = headB
		while p1 and p2:
			p1 = p1.next
			p2 = p2.next
			if p2: p2 = p2.next
			if p1 == p2: break
		
		pdb.set_trace()
		if p1 and p2 and p1 == p2:
			p1 = headB
			while p1 != p2:
				p1 = p1.next
				p2 = p2.next
			rst = p1

		#unmake the cycle
		mark.next = None

		return rst

if __name__ == '__main__':
	headA = ListNode(1)
	headA.next = ListNode(2)
	headA.next.next = ListNode(3) 
	headA.next.next.next = ListNode(4) 
	tmp = headA.next.next.next.next = ListNode(5) 

	headB = ListNode(6)
	headB.next = ListNode(7)
	headB.next.next = tmp
	tmp.next = ListNode(8)

	sol = Solution()
	rst = sol.getIntersectionNode(headA, headB)
	print rst.val

	headC = ListNode(2)
	headC.next = ListNode(3)
	headD = ListNode(5)
	sol.getIntersectionNode(headC, headD)
