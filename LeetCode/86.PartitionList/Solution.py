# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        headLess = None
        headGreat = None
        pless = None
        pgreat = None
        
        p = head
        while p:
            tmp = p.next
            p.next = None
            if p.val < x:
                if not headLess: 
                    headLess = p
                    pless = headLess
                else:
                    pless.next = p
                    pless = p
            else:
                if not headGreat:
                    headGreat = p
                    pgreat = headGreat
                else:
                    pgreat.next = p
                    pgreat = p
            p = tmp
        if not headLess: return headGreat
        if headLess:
            pless.next = headGreat
            return headLess
