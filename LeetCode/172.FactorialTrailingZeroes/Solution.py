class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        rst = 0
        while n > 0:
            rst += n / 5
            n /= 5
        return rst 
