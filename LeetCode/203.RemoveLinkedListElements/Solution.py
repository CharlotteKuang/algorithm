class Solution:
	# @param {ListNode} head
	# @param {integer} val
	# @return {ListNode}
	def removeElements(self, head, val):
		pre = ListNode(0)
		pre.next = head
		cur = head
		new_head = pre

		while cur:
			next_node = cur.next
			if cur.val == val:
				pre.next = next_node
				del(cur)
			else:
				pre = cur
			cur = next_node 
			result = new_head.next
			del(new_head)
		return result
