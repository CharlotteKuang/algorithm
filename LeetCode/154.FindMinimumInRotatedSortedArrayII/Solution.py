class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # follow your gut
        if len(nums) == 1: return nums[0]

        head, tail = 0, len(nums)-1
        while head+1 < tail:
            mid = head + (tail-head)/2
            if nums[mid] > nums[tail]:
                    head = mid
            else:
                if nums[mid] == nums[tail]:
                    m1 = self.findMin(nums[head:mid+1])
                    m2 = self.findMin(nums[mid:tail+1])
                    return min(m1, m2)
                else:
                    tail = mid
        return min(nums[head], nums[tail])
