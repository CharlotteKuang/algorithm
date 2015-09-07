class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a, c = None, 0
        for n in nums:
            if c == 0:
                a, c = n, 1
            elif a == n:
                c += 1
            else:
                c -= 1
        return a
