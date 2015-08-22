import copy

class Solution(object):
    def subsets_helper(self, nums, subset, count):
        if len(subset) == count:
            self.subsets.append(copy.copy(subset))
        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i-1]: continue
            subset.append(nums[i])
            self.subsets_helper(nums[i+1:], subset, count)
            subset.pop()
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        self.subsets = []
        for i in range(0, len(nums)+1):
            self.subsets_helper(nums, [], i)
        return self.subsets
