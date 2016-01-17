import pdb
from List import List

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """ 
        if not head or not head.next:
            return head

        oddHead = head 
        evenHead = head.next 
        oddPointer = oddHead
        evenPointer = evenHead 
        oddHead.next = None
        p = evenPointer.next
        evenPointer.next = None 
        count = 3

        while p:
            if count & 1:
                oddPointer.next = p
                oddPointer = oddPointer.next
            else:
                evenPointer.next = p
                evenPointer = evenPointer.next
            tmp = p.next
            p.next = None
            p = tmp
            count += 1
        oddPointer.next = evenHead

        return oddHead

if __name__ == '__main__':
    myList = List([1,2,3,4,5,6])
    sol = Solution()
    myList.apply(sol.oddEvenList)
    print myList.getValues()

    myList = List([1,2,3,4,5])
    sol = Solution()
    myList.apply(sol.oddEvenList)
    print myList.getValues()

    myList = List([1,2,3,4])
    sol = Solution()
    myList.apply(sol.oddEvenList)
    print myList.getValues()

    myList = List([1,2,3])
    sol = Solution()
    myList.apply(sol.oddEvenList)
    print myList.getValues()

    myList = List([1,2])
    sol = Solution()
    myList.apply(sol.oddEvenList)
    print myList.getValues()

    myList = List([1])
    sol = Solution()
    myList.apply(sol.oddEvenList)
    print myList.getValues()

    myList = List([])
    sol = Solution()
    myList.apply(sol.oddEvenList)
    print myList.getValues()
