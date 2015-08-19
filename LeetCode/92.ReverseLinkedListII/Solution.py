import pdb
# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param {ListNode} head
	# @param {integer} m
	# @param {integer} n
	# @return {ListNode}
	def reverseBetween(self, head, m, n): 
		pm, pn, mprev = None, None, None
		p = head
		count = 1
		while count < m and p:
			mprev = p
			p = p.next
			count += 1
		if not p: return head 

		pm = p
		prev = p
		p = p.next
		count += 1

		while count <= n and p:
			tmp = p.next
			p.next = prev
			prev = p
			p = tmp
			count += 1
		
		pn = prev
		if mprev:
			mprev.next = pn
		else: head = pn
		pm.next = p

		return head

def makeListByArray(arr):
	if len(arr) == 0: return None

	head = ListNode(1)
	p = head
	for i in arr[1:]:
		p.next = ListNode(i)
		p = p.next
	return head

def printList(head):
	result = []
	p = head
	while p:
		result.append(p.val)
		p = p.next
	print result 

if __name__ == '__main__':
	sol = Solution()
	head4 = makeListByArray([1,2,3,4,5])
	head4 = sol.reverseBetween(head4, 1, 4)
	printList(head4)

	head = makeListByArray([1,2,3,4,5,6,7])
	head = sol.reverseBetween(head, 2, 4)
	printList(head)

	head2 = makeListByArray([1,2,3,4,5])
	head2 = sol.reverseBetween(head2, 6, 7)
	printList(head2)

	head3 = makeListByArray([1,2,3,4,5])
	head3 = sol.reverseBetween(head2, 4, 7)
	printList(head3)
	
	sol.reverseBetween(None, 1, 3)
