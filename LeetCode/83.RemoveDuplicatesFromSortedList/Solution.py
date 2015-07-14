class Solution:
	# @param {ListNode} head
	# @return {ListNode}
	def deleteDuplicates(self, head):
		if head is None: return None
			pre = head
			cur = head.next
		while cur:
			if cur.val == pre.val:
				pre.next = cur.next
				del(cur)
			else:
				pre = cur
			cur = pre.next
		return head
