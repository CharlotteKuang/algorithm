from math import fabs
from pdb import set_trace as debug

class Solution:
	# @param {integer[]} nums
	# @param {integer} target
	# @return {integer}
	def threeSumClosest(self, nums, target):
		result = nums[0]+nums[1]+nums[2]
		length = len(nums)
		nums.sort()
		#debug()
		for i in range(0, length-2):
			p1 = i+1
			p2 = length-1
			tmp = nums[i]+nums[p1]+nums[p2]
			while p1 < p2:
				s = nums[i]+nums[p1]+nums[p2]
				if s == target:
					return target
				else:
					if fabs(tmp-target) < fabs(s-target):
						break
					else:
						tmp = s
						if s < target:
							p1 += 1
						else:
							p2 -= 1
			if fabs(tmp-target) < fabs(result-target):
				result = tmp
		return result 
