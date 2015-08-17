import pdb
# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        p = head
        p2 = head
        try:
            while p and p2:
                p = p.next
                p2 = p2.next
                p2 = p2.next
                if p == p2: return True
        except AttributeError:
            return False
        return False

h = ListNode(1)
h.next = h
sol = Solution()
print sol.hasCycle(h)
