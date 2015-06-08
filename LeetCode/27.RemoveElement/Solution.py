class Solution:
	# @param {integer[]} nums
	# @param {integer} val
	# @return {integer}
	def removeElement(self, nums, val):
		p = 0
		for i in range(len(nums)):
			if nums[i] != val:
				nums[p] = nums[i]
				p += 1
		return p		

