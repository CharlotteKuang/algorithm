# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class List(object):
    def __init__(self, array_of_values):
        head = None
        p = None
        for value in array_of_values:
            if not head:
                head = ListNode(value)
                p = head
            else:
                p.next = ListNode(value)
                p = p.next
        self.__list__ = head

    def getList(self):
        return self.__list__

    def getValues(self):
        values = []
        p = self.__list__
        while p:
            values.append(p.val)
            p = p.next
        return values

    def apply(self, func):
        self.__list__ = func(self.__list__)
