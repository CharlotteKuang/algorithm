class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        tmp = []
        while not self.empty():
            tmp.insert(0, self.peek())
            self.pop()
            
        self.queue.append(x)
        while len(tmp):
            self.queue.insert(0, tmp[0])
            tmp.pop(0)

    def pop(self):
        """
        :rtype: nothing
        """
        if len(self.queue) > 0:
            self.queue.pop(0)

    def peek(self):
        """
        :rtype: int
        """
        return self.queue[0] if len(self.queue) else None
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue) == 0
