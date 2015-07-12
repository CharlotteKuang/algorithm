#Finding the first missing positive.
#I will first sorted the array, then iterate the sorted array and find i where i < len(nums) and nums[i]-1 does not equal to i. I am using the index to place the integers. Then I can solve this problem without sorting array, swapping the elements instead.

class Solution:
	# @param {integer[]} nums
	# @return {integer}
	def firstMissingPositive(self, nums): 
		if not nums: return 1
		for i in range(len(nums)):
			while nums[i] > 0 and nums[i] != i+1 and nums[i]-1 < len(nums) and nums[i] != nums[nums[i]-1] :
				pos = nums[i]-1
				nums[i], nums[pos] = nums[pos], nums[i]
		for i in range(len(nums)):
			if nums[i]-1 != i: return i+1
		return len(nums)+1
