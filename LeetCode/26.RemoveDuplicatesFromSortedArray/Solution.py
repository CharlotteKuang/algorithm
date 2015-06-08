class Solution:
	# @param {integer[]} nums
	# @return {integer}
	def removeDuplicates(self, nums): 
		if len(nums) <= 1: return len(nums) 
		p = 0
		for i in range(1, len(nums)):
			if nums[p] != nums[i]:
				nums[p+1] = nums[i]
				p += 1
		return p + 1
