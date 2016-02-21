import sys

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3: return False
        a0 = nums[0]
        a2 = sys.maxint
        for a in nums[1:]:
            if a <= a0: a0 = a
            else:
                if a < a2: a2 = a
                elif a > a2: return True
        return False
