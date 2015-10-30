class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        c0, c1, c2 = 0, 0, 0
        for i in nums:
            if i == 0: c0 += 1
            if i == 1: c1 += 1
            if i == 2: c2 += 1
        start = 0
        
        for i in range(c0):
            nums[start] = 0
            start += 1
            
        for i in range(c1):
            nums[start] = 1
            start += 1
        
        for i in range(c2):
            nums[start] = 2
            start += 1
            
            
