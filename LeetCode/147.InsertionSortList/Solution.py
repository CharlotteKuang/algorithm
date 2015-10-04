# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        
        rst = head
        p = rst.next
        rst.next = None
        
        while p:
            tmp = p.next
            insertionPos = rst
            pre = None
            while insertionPos and p.val > insertionPos.val:
                pre = insertionPos
                insertionPos = insertionPos.next
            if not pre:
               p.next = rst
               rst = p
            else:
                p.next = insertionPos
                pre.next = p
            p = tmp
        return rst
        
