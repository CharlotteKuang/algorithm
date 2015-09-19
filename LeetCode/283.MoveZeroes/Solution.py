class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums):
            pos = 0
            nonZeroPos = 0
            count = 0
            while pos < len(nums):
                if nums[pos]:
                    nums[nonZeroPos] = nums[pos]
                    nonZeroPos += 1
                else:
                    count += 1
                pos += 1
            for i in range(count):
                nums[nonZeroPos+i] = 0
