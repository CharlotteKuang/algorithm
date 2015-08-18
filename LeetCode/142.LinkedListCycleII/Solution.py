import pdb
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        pdb.set_trace()
        p1 = head
        p2 = head
        try:
            while p1 and p2:
                p1 = p1.next
                p2 = p2.next
                p2 = p2.next
                if p1 == p2:
                    break
        except AttributeError:
            return None
        p1 = head
        while p1 and p2 and p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1

if __name__ == '__main__':
    h = ListNode(1)
    h2 = ListNode(2)
    sol = Solution()
    h.next = h2
    print sol.detectCycle(h)
