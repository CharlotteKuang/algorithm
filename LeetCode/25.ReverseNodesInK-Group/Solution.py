import pdb
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head: return
        count = 0
        p = head        
        while p:
            count += 1
            p = p.next
        segments = count / k
        #pdb.set_trace()
        
        count = 0
        p, pre = head, None
        tmp = None 
        rst = head
        while count < segments:
           sc = 1
           last = p
           sp = p
           p = p.next
           while sc < k:
               tmp = p.next
               p.next = sp   
               sp = p
               p = tmp
               sc += 1
           if not pre: rst = sp 
           if pre:
              pre.next = sp
           pre = last
           count += 1
        if pre: pre.next = p
        return rst

def makeListByArray(array):
    if not array: return None
    head = ListNode(array[0])
    p = head
    for n in array[1:]:
        p.next = ListNode(n)
        p = p.next
    return head

def printList(head):
    p = head
    while p:
       print p.val
       p = p.next

if __name__ == '__main__':
    sol = Solution()
    head = makeListByArray([1,2,3,4,5,6,7])
    rst = sol.reverseKGroup(head, 2)
    printList(rst) 

    print 

    head = makeListByArray([1,2,3,4,5,6,7])
    rst = sol.reverseKGroup(head, 4)
    printList(rst) 

    print 

    rst = sol.reverseKGroup(None, 4)
    printList(rst) 

    print 

    head = makeListByArray([1])
    rst = sol.reverseKGroup(head, 2)
    printList(rst) 
