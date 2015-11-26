class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # follow your gut
        #if len(nums) == 1: return nums[0]
        return self.helper(nums, 0, len(nums)-1)
    def helper(self, nums, head, tail):
        while head+1 < tail:
            mid = head + (tail-head)/2
            if nums[mid] > nums[tail]:
                    head = mid
            else:
                if nums[mid] == nums[tail]:
                    m1 = self.helper(nums, head, mid)
                    m2 = self.helper(nums, mid, tail)
                    return min(m1, m2)
                else:
                    tail = mid
        return min(nums[head], nums[tail])
