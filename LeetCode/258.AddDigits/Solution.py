class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10: return num
        tmp = 0
        while num > 0:
            tmp += num % 10
            num /= 10
        return self.addDigits(tmp)
        
