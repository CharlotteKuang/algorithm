class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    '''
        def reverseList(self, head):
        if head is None: return None
        if head.next is None: return head
        tmp = head.next
        reverse = self.reverseList(tmp)
        tmp.next = head
        head.next = None
        return reverse
        '''
    def reverseList(self, head):
        if head is None: return None
        if head.next is None: return head
        p1 = head
        p2 = head.next
        while p2:
            tmp = p2.next
            p2.next = p1
            p1 = p2
            p2 = tmp
        head.next = None
        return p1
