import random
import sys
import pdb

# Definition for singly-linked list.
class ListNode(object):
	 def __init__(self, x):
		 self.val = x
		 self.next = None

class Solution(object):
	def sortList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		""" 
		if not head: return None

		if not head.next: return head

		p1, p2 = head, head
		pre = None

		#pdb.set_trace()
		while p1 and p2:
			pre = p1
			p1 = p1.next
			p2 = p2.next
			p2 = p2.next if p2 else None

		#pdb.set_trace()

		pre.next = None
		l1 = self.sortList(head)
		l2 = self.sortList(p1)

		#pdb.set_trace()

		t1, t2 = l1, l2
		rst = None
		p = None 

		while t1 and t2:
			if t1.val < t2.val:
				if not rst:
					rst = t1
					p = rst
				else:
					p.next = t1
					p = p.next
				t1 = t1.next
			else:
				if not rst:
					rst = t2
					p = rst
				else:
					p.next = t2
					p = p.next
				t2 = t2.next
		if not t1: 
			p.next = t2
		elif not t2:
			p.next = t1
		return rst

if __name__ == '__main__':
	sys.path.append('/Users/kwj/Documents/code/algorithm/algorithm/LeetCode/helper')
	from List import *
	helper = ListNodeHelper()
	
	numCount = random.randint(0, 5000)
	nums = []
	for i in range(numCount):
		nums.append(random.randint(0, 5000))

	ls = helper.makeList(nums)
	#print helper.printList(ls)

	sol = Solution() 
	rst = sol.sortList(ls) 
	print helper.printList(rst)
