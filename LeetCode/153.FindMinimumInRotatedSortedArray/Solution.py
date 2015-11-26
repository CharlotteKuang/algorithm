class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #return min(nums)
        if len(nums) == 1: return nums[0]
        
        head, tail = 0, len(nums)-1
        while head+1 < tail:
            mid = head + (tail-head)/2
            if nums[mid] > nums[tail]:
                    head = mid
            else: tail = mid
        return min(nums[head], nums[tail])
