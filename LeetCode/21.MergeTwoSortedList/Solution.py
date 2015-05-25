# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        result = None
        p = result
        p1 = l1
        p2 = l2
        while p1 is not None and p2 is not None:
            smaller = min(p1.val, p2.val)
            if result is None:
                result = ListNode(smaller)
                p = result
            else:
                p.next = ListNode(smaller)
                p = p.next
            if smaller == p1.val: p1 = p1.next
            else: p2 = p2.next
        if p1 is not None: pt = p1
        else: pt = p2
        while pt is not None:
            if result is None:
                result = ListNode(pt.val)
                p = result
            else:
                p.next = ListNode(pt.val)
                p = p.next
            pt = pt.next
        return result
