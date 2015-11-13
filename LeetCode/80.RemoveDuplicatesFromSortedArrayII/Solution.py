import pdb
class Solution(object):
	def removeDuplicates(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if not nums:
			return 0
		p1, p2 = 0, 0
		last = 1
		for i in range(1, len(nums)):
			if nums[i] == nums[i-1]:
				if p1 == p2: 
					p2 = i
				else: continue
			else:
				p1, p2 = i, i
			nums[last] = nums[i]
			last += 1
		return last

if __name__ == '__main__':
	cases = [
		[],
		[1,2,3],
		[1,1,1,2,3,4,4,5],
		[1,1,2,2,2,3,4,4,5],
		[1,1,2,2,2,3,4,4,5,6,6,6,6,7,7,7,8],
	]

	sol = Solution()
	for case in cases:
		length = sol.removeDuplicates(case)
		print case[0:length]
